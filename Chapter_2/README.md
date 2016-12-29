### Chapter Overview 
This chapter covers two straight forward distance metrics that will be used throughout the rest of the book, Euclidian and Pearson. It also goes indepth into various filtering methods that are applied to a dataset of movie reviews.

### Code Usage
*import recommendations 

* ``sim_distance(dataset, A, B)``
Calculatse the euclidian distance between A and B in the dataset

* ``sim_pearson(dataset, A, B)``
Calculates the pearson distance between A and B in the dataset

* ``topMatches(dataset, A, n=3)``
Returns the top n items in the dataset similar to A

* ``getRecommendations(dataset, A, similarity=[optional])``
Returns similar items to A that are not in A but are in the dataset. Interesting to use multiple similarity functions and see how they determine different best fits
  
* ``transformPrefs(dataset)``
Switches the row's and col's. Can generate interesting results 

* ``calculateSimilarItems(dataset)``
Returns an new itemset of similar items to each item. Takes awhile but does 
not need to be done often.

* ``getRecommendedItems(dataset, itemset, A)``
Returns recommended items for A based off of the itemset. 

* ``loadMovieLens()``
Helper function for reading in the MovieLens dataset'

