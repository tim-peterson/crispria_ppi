# crispria_ppi
intersecting selection pressure, growth-based CRISPRi/a data with existing PPIs to predict novel PPIs


v1

v2

v3

v4

v5

v6 only using the 3 weissman CRISPRi/a datasets to train the model

v7 multiplying rho's

v8 multiplying rho's not taking abs() value of them

got rid of sigmoid activation in output layer so predictions aren't binary but rather a scale.

v9 use Huttlin Compass scores rather than binary 0/1 binding no binding

Result: debatable whether v8 or v9 is better. v8 (binary huttlin scoring) gets slightly more interactions. Is raptor mTOR's best interactor?

v10 TO-DO: We need negative controls to prove that random gene X like HSD17B12 doesn't just bind every gene. get probabilities for all 20,000 protein coding genes. 

v11 test using std dev. outliers rather than p < 0.05 in training data counting towards huttlin positivity 
compare vs. primary DNA/protein sequence-based predictions