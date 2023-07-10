import scipy.io


def import_data():
    dat = scipy.io.loadmat("dat1.mat")
    test_size = 200
    length = dat["A"].shape[0]
    x_train = dat["A"][0:length-test_size]
    y_train = dat["B"][0:length-test_size]
    x_test = dat["A"][-test_size:]
    y_test = dat["B"][-test_size:]
    return x_train, y_train, x_test, y_test
