rmf ./output-positive
rmf ./output-negative
rmf ./output-step-1a
rmf ./output-step-1b
rmf ./output-step-1c
rmf ./output-step-2a
rmf ./output-step-2b

-- load and parse JSON input file
R = LOAD 'yelp_review.json' USING JsonLoader('votes:map[], user_id:chararray, review_id:chararray, stars:int, date:chararray, text:chararray, type:chararray, business_id:chararray');

-- read the review field, and generate token (word) list
-- by wordbreaking on the given characters in the regexp
B0 = foreach R generate flatten(TOKENIZE(LOWER(REPLACE($5, '[\\s\\.\\,\\!\\?\\-]+', ' ')))) as word, stars;

STORE B0 INTO './output-step-0';

C = foreach B0 generate word, 1 as total_freq, stars;

-- filter out all, positive, and negative review group data
D1 = filter C by stars >= 0;
D2 = filter C by stars >= 5;
D3 = filter C by stars <= 2;

F1 = group D1 by word;
F2 = group D2 by word;
F3 = group D3 by word;

-- generate word counts for all, positive, and negative groups
G1 = foreach F1 generate group as word1, SUM(D1.total_freq) as total_freq1;
G2 = foreach F2 generate group as word2, SUM(D2.total_freq) as total_freq2;
G3 = foreach F3 generate group as word3, SUM(D3.total_freq) as total_freq3;

STORE G1 INTO './output-step-1a';
STORE G2 INTO './output-step-1b';
STORE G3 INTO './output-step-1c';

-- only keep most frequent words
Z1 = filter G1 by $1 > 1000;

-- compute total frequencies over all words in each group
NORM1 = GROUP G1 ALL;
NORMF1 = foreach NORM1 generate SUM(G1.total_freq1) as overall_freq1;

NORM2 = GROUP G2 ALL;
NORMF2 = foreach NORM2 generate SUM(G2.total_freq2) as overall_freq2;

NORM3 = GROUP G3 ALL;
NORMF3 = foreach NORM3 generate SUM(G3.total_freq3) as overall_freq3;

H1 = join Z1 by word1, G2 by word2;
H2 = join Z1 by word1, G3 by word3;

STORE H1 INTO './output-step-2a';
STORE H2 INTO './output-step-2b';

-- generate positive and negative word probabilities
I1  = foreach H1 generate $0, $3, $1, $3/(double)NORMF2.overall_freq2, $1/(double)NORMF1.overall_freq1;

I2  = foreach H2 generate $0, $3, $1, $3/(double)NORMF3.overall_freq3, $1/(double)NORMF1.overall_freq1;

-- generate positive and negative log ratios
IBEST = foreach I1 generate $0, LOG($3)-LOG($4) as ratio_best;
JBEST = ORDER IBEST by ratio_best DESC;
IWORST = foreach I2 generate $0, LOG($3)-LOG($4) as ratio_worst;
JWORST = ORDER IWORST by ratio_worst DESC;

-- write out final lists
STORE JBEST INTO './output-positive'; 
STORE JWORST INTO './output-negative'; 