#The purpose of this program is to get the pre_market prices and output them into a file
 
#Updates:
#3/13/2015: Program was created
#3/23/2015: A new try/except statement was created as the previous version couldn't pull pre-market data if there weren't any. Also the last for loop that took care of writing to the file was deleted and added to the loop that pulled the stock prices for simplicity.
#3/30/2105: made a new try and except so that if you cannot pull the source code then the except will set the pre_market_price[0] to "N/A"
 
 
 
 
#This section imports all necessary libraries for the code to run properly
import urllib.request from urllib2
import time
 
def main():
    print("starting the program")
    print("please enter the tickers you want the premarket prices for. enter 'QUIT' or 'quit' to finish entering the tickers")
    endOfTickers = False
    counter = 1
    tickers = []
    while(endOfTickers == False):
        ticker = input("Please enter ticker #" + counter)

        #checking to see if the user wants to finish entering the ticker symbol.
        if(ticker != "QUIT" or ticker != "quit"):
            tickers.append(ticker)
        else:
            endOfTickers = True



    file = open("pre_market_stock_prices.txt", "w") #Writes over the previous file with new information
   
    stock_prices = []
    pre_market_price = []
    for j in range(0, len(tickers) - 1):
        tickers[j] = str(tickers[j])
        tickers[j] = tickers[j].lower()
   
    #Starts a loop through all tickers where it will find the sourceCode from yahoo finance to get the stock prices
    for i in range(0, len(tickers) - 1):
        time.sleep(2) #The program will pause once it hits this point for 2 seconds just so we don't hammer the yahoo servers
        url = "http://finance.yahoo.com/q?s=" + tickers[i] #The URL where the stock prices can be found at
        try:
            sourceCode = urllib.request.urlopen(url) #opens the source code
            x = sourceCode.read() #reads the source code into another variable
            sourceCode.close() #closes the file for the source code      
            try:
                x = str(x) #converting the source code into a string format
                first_price = x.split('<span id="yfs_l86_' + tickers[i] + '">') #The first split - alternative for current price <span id="yfs_l84_'
                pre_market_price  = first_price[1].split("</span>") #The second split where it will seperate the stock price from the rest of the HTML file
            except Exception:
                x = str(x) #converting the source code into a string format
                first_price = x.split('<span id="yfs_l84_' + tickers[i] + '">') #The first split - alternative for current price <span id="yfs_l84_'
                pre_market_price  = first_price[1].split("</span>") #The second split where it will seperate the stock price from the rest of the HTML file
        except Exception:
            pre_market_price[0] = "N/A"
        stock_prices.append(pre_market_price[0]) #Entering the price into the list that contains all of the stock prices
        print(tickers[i], "   ", stock_prices[i])
       
        file.write(tickers[i] + "," + str(stock_prices[i]) + "\n") #Writes information into the file
    run_time = str(time.asctime())
    run_time = "Time: " + run_time
    file.write(run_time)
    print("complete")
    file.close() #closes the file
    time.sleep(1)
main() #End of program
