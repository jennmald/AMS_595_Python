import sys
import csv
## Parses command line from raw input
## Params: raw_command_line - raw input
## Returns: files - the csv files to parse
## Design Idea:
## I wanted to change up this method and include a case
## where the user didn't enter any files 
## this would make the raw input length 1
## from there I included the case where there 
## was only one file input and finally
## the list of files for more than 1 csv input
def parse_command_line(raw_command_line):
	# check length
	rawlength = len(raw_command_line)
	files = [] #create empty list to store file names
	if rawlength == 1: # case: no input files
		files = None
		print('No files specified')
	elif rawlength == 2: # case: 1 input files
		files.append(raw_command_line[1])
	else: # case: multiple input files
		for i in range(1,rawlength):
			files.append(raw_command_line[i])
	return files

def parse_csv(filename):
	# create a dictionary to hold all companies
	company_dict = {}
	# open file
	open_file = open(filename)
	# use csv reader with delimiter , to parse csv file
	each_line = csv.reader(open_file, delimiter=',')
    	# read each row and determine the company name
	for row in each_line:
		case = row[0].upper()
		if case not in company_dict: # if different company initialize it's data
			company_dict[case] = [[row[1]], [row[2]], [row[3]]]
		else: # keep appending to the already initialized data
			company_list = company_dict[case]
			company_list[0].append(row[1])
			company_list[1].append(row[2])
			company_list[2].append(row[3])
	largest_client = {}
	# remove the titles
	company_dict.pop('CLIENTNAME')
	# start computing the aggregate sales
	for key in company_dict:
		company_info = company_dict[key] # the list of quantity,price, date
		quantity = company_info[0] # quantity
		price = company_info[1] # price
		if key not in largest_client: # start adding to the dictionary
			# initialize
			largest_client[key] = float(quantity[0])*float(price[0])
		for i in range(1, len(quantity)): # add the rest
			agg = largest_client[key] # update the aggregate total
			new_agg = agg + (float(quantity[i])+float(price[i]))
			largest_client[key] = new_agg
	maximum = 0 # set low value for max so first company becomes max
	max_company  = '' # to store company name
	print('Aggregate Sales Revenue') # heading
	for key in largest_client: #  find the maximum
		if largest_client[key] > maximum:
			maximum = largest_client[key]
			max_company = key
		# print each company and aggregate revenue
		print('The company ' + key + ' has aggregate revenue of ' + str(largest_client[key]))
	# print maximum
	print(' ')
	print('Maximum Aggregate Sales Revenue')
	print('The company ' + max_company + ' had the largest aggregate at ' + str(maximum))
	print(' ')
	print('Monthly Sales:')
	# deal with monthly sales now
	for key in company_dict: # iterate through again
		company_info = company_dict[key]
		quantity = company_info[0] # grab quantity list
		price = company_info[1] #grab price list
		date_list = company_info[2] # grab the date list
		date_dict = {} # dictionary for dates
		for d in range(0, len(date_list)):
			full_date = date_list[d]
			year = full_date[0:4] # year
			month = full_date[5:7] # month
			if year not in date_dict: # store by year
				date_dict[year] = {}
			total_months = date_dict[year]
			if month not in total_months: # monthly aggregate
				total_months[month] = float(quantity[d])*float(price[d])
			else: # update monthly aggregate
				current = total_months[month]
				updated = current + (float(quantity[d])*float(price[d]))
		# get the last day of the month
		day_month = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30', '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}
		for k in date_dict: # iterate through and print
			print('For company '+ key + ' the year ' + k + ' the monthly sales were:')
			monthly_revenue = date_dict[k]
			for m in monthly_revenue:
				print(m + '/'+ day_month[m]+ ': ' + str(monthly_revenue[m]))
if __name__ == "__main__":
    files_to_parse = parse_command_line(sys.argv)
    # to parse multiple files
    # works for multiple files separated by spaces
    for last_file in files_to_parse:
    	print("Beginning parse of", last_file)
    	parse_csv(last_file)