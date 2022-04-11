from train import train

def test_me():
    accuracy_score = train(max_depth=5)
    print("Test: accuracy_score:",accuracy_score)

