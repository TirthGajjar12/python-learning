def transaction_stream():
    while  True:
        transactions =  input("Enter a transaction amount (or type 'done to finish'): ").lower()
        if transactions ==  'done' or transactions == 'finish':
            break
        else:
            transactions = int(transactions)
            yield transactions

def audit_function(func):
    def wrappper(*args,**kargs):
        print("Audit : Processing strated...")
        result = func(*args,**kargs)
        print("audit : Process complete.")
        return result
    return wrappper

class dataPipline():

    def __init__(self,**kwargs):
        self.__settings = kwargs

    @audit_function
    def process_transaction(self,dataList):
        data = map(lambda x:x * 1.18,dataList)
        final_list = list(data)
        return final_list


pipeline = dataPipline(country = 'india', tax = 'gst')
raw_data = list(transaction_stream())
final_price = pipeline.process_transaction(raw_data)
print(final_price)




