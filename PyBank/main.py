import csv
import statistics

pullfile = 'budget_data_1.csv'
pushfile = 'PyBankResults_SL.txt'

with open(pullfile, newline='') as csvfile:
	
	csvreader = csv.reader(csvfile, delimiter = ',')
	
	#skip first line
	next(csvfile)

	totalmonths = 0
	totalrevenue = 0
	prevrevenue = 0
	revenuechange = 0
	revenuediffs = {}
	greatincrev = 0
	greatdecrev = 0
	greatincmth = ""
	greatdecmth = ""

	for row in csvreader:

		#The total number of months included in the dataset
		totalmonths = totalmonths + 1

		#The total amount of revenue gained over the entire period
		current_revenue = row[1]
		totalrevenue = totalrevenue + int(current_revenue)

		current_month = row[0]

		#Calculate revenue change and store it in dictionary
		if (prevrevenue > -1000000000):
			revenuechange = int(current_revenue) - prevrevenue
			revenuediffs[current_month] = revenuechange
		else:
			revenuechange = int(current_revenue)
			revenuediffs[current_month] = revenuechange

		prevrevenue = int(current_revenue)

	#The average change in revenue between months over the entire period
	avg_revenuechange = statistics.mean(revenuediffs.values())

	for month in revenuediffs:
		revchange = revenuediffs[month]
	#The greatest increase in revenue (date and amount) over the entire period
		if (revchange > greatincrev):
			greatincrev = revchange
			greatincmth = month
	
	#The greatest decrease in revenue (date and amount) over the entire period
		if (revchange < greatdecrev):
			greatdecrev = revchange
			greatdecmth = month

	print ("Financial Analysis")
	print ("-------------------------")
	print ("Total Months: " + str(totalmonths))
	print ("Total Revenue: $" + str(totalrevenue))
	print ("Average Revenue Change: $" + f"{avg_revenuechange:.2f}")
	print ("Greatest Increase in Revenue: "+greatincmth+ " ($" + str(greatincrev) + ")")
	print ("Greatest Decrease in Revenue: "+greatdecmth+ " ($" + str(greatdecrev) + ")")

with open(pushfile, "w") as txt_file:	

	txt_file.write("Financial Analysis\n")
	txt_file.write("-------------------------\n")
	txt_file.write("Total Months: " + str(totalmonths)+"\n")
	txt_file.write("Total Revenue: $" + str(totalrevenue)+"\n")
	txt_file.write("Average Revenue Change: $" + f"{avg_revenuechange:.2f}\n")
	txt_file.write("Greatest Increase in Revenue: "+greatincmth+ " ($" + str(greatincrev) + ")\n")
	txt_file.write("Greatest Decrease in Revenue: "+greatdecmth+ " ($" + str(greatdecrev) + ")\n")