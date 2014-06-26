

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.common.FastByIDMap;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.ThresholdUserNeighborhood;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.model.Preference;
import org.apache.mahout.cf.taste.model.PreferenceArray;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.recommender.UserBasedRecommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;
import org.apache.mahout.cf.taste.impl.recommender.GenericBooleanPrefItemBasedRecommender;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.LogLikelihoodSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.impl.model.GenericDataModel;
import org.apache.mahout.cf.taste.impl.model.GenericPreference;
import org.apache.mahout.cf.taste.impl.model.GenericUserPreferenceArray;
import org.apache.mahout.cf.taste.impl.model.MemoryIDMigrator;
import org.apache.commons.csv.CSVParser;


public class App 
{
	private Recommender recommender = null;
    private MemoryIDMigrator thing2long = new MemoryIDMigrator();
    private static String DATA_FILE_NAME = "C:/Users/Kri89/Desktop/dataset.csv";
    private static DataModel dataModel;
    public void initRecommender() {
        try {
            String[] line;
            Map<Long,List<Preference>> preferecesOfUsers = new HashMap<Long,List<Preference>>();
            // a CSV parser for reading the file
            CSVParser parser = new CSVParser(new InputStreamReader(new FileInputStream(DATA_FILE_NAME), "UTF-8"));
            // exclude the header which we are not considering
            String[] header = parser.getLine();
            // go through every line
            while((line = parser.getLine()) != null) {
                List<Preference> userPrefList;
                String person = line[0];
                String likeName = line[1];
                // store the mapping for the user
                long userLong = thing2long.toLongID(person);
                thing2long.storeMapping(userLong, person);
                // store the mapping for the item
                long itemLong = thing2long.toLongID(likeName);
                thing2long.storeMapping(itemLong, likeName);
                if((userPrefList = preferecesOfUsers.get(itemLong)) == null) {
                    userPrefList = new ArrayList<Preference>();
                    preferecesOfUsers.put(itemLong, userPrefList);
                }
                // add the similarities found to this user
                userPrefList.add(new GenericPreference(itemLong, userLong, 1));
            }
            // create the corresponding mahout data structure from the map
            FastByIDMap<PreferenceArray> preferecesOfUsersFastMap = new FastByIDMap<PreferenceArray>();
            for(Entry<Long, List<Preference>> entry : preferecesOfUsers.entrySet()) {
                preferecesOfUsersFastMap.put(entry.getKey(), new GenericUserPreferenceArray(entry.getValue()));
            }
            // create a data model
            dataModel = new GenericDataModel(preferecesOfUsersFastMap);
            // Recommender Instantiation
            recommender = new GenericBooleanPrefItemBasedRecommender(dataModel, new LogLikelihoodSimilarity(dataModel));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public String[] recommendThings(String personName) throws TasteException {
        List<String> recommendations = new ArrayList<String>();
        try {
            /*
             * value passed are the search term and the number of recommendations needed.
             * in this case, it is 10
             */
            List<RecommendedItem> items = recommender.recommend(thing2long.toLongID(personName), 2);
            for(RecommendedItem item : items) {
                recommendations.add(thing2long.toStringID(item.getItemID()));
            }
        } catch (TasteException e) {
            throw e;
        }
        return recommendations.toArray(new String[recommendations.size()]);
    }
    public static void main(String[] args) {
        System.out.println("——RECOMMENDATION——\n\n");
        App hlReco = new App();
        hlReco.initRecommender();
        try {
            for (String result : hlReco.recommendThings("Facebook")) {
                System.out.println(result);
            }
        } catch (TasteException e) {
            e.printStackTrace();
        }
    }
}	
	