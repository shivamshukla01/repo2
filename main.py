from wazirx import wazirx
from zebpay import zebpay
from coindcx import coindcx
from collect import collect
from bitbns import bitbns

def main():
    count=1
    while(True):
        wazirx()
        zebpay()
        coindcx()
        bitbns()
        buyucoin()
        collect()
        print("Iteration=",count)
        count=count+1

if __name__ == "__main__":
    main()
