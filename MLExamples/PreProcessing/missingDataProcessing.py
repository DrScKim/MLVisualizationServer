import numpy as np

EXAMPLE_DATA = np.array([[1., 2., 3., 4., ],
                         [5.,6.,np.nan,8.],
                        [5.,6.,7,8.],
                         [10.,11.,12.,np.nan]])

def removeRow_containNaN(npArray):
    return npArray[~np.isnan(npArray).any(axis=1)]

def test_removeRow_containNaN(npArray):
    print('Original matrix')
    print(npArray)
    processed_data = removeRow_containNaN(npArray)
    print("Conduct remove NaN\n")
    print(processed_data)

def impute_NaN(npArray, _strategy='mean'):
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan, strategy=_strategy, verbose=0)
    imputer = imputer.fit(npArray)
    imputed_data = imputer.transform(npArray)
    print(imputed_data)

def test_impute_NaN(npArray):
    strategies = ['mean', 'most_frequent', 'median']
    for strategy in strategies:
        print("%s result:" % strategy)
        impute_NaN(npArray, strategy)
        print("===========")

if __name__ == "__main__":
    test_removeRow_containNaN(EXAMPLE_DATA)
    test_impute_NaN(EXAMPLE_DATA)
