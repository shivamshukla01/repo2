from createtables import createtables
from wazirx import wazirx
from zebpay import zebpay
from coindcx import coindcx
from collect import collect
from bitbns import bitbns
from buyucoin import buyucoin

def main():
    try:
        createtables()
    except:
        print("An exception occurred(Tables already created)")
    count=1
    while(True):
        try:
            wazirx()
            zebpay()
            coindcx()
            bitbns()
            buyucoin()
            collect()
            print("Iteration=",count)
            count=count+1
        except:
            print("An exception occurred")
            continue

if __name__ == "__main__":
    main()
