# ----Requirements----
# grab
# pycurl
# lxml
def write_to_file(file, exchange_rate):
	import datetime
	with open(file, mode = 'a+') as file_for_write: 
		list_for_numbering = [] 
		data = str(datetime.datetime.today().date()) # today date
		
		if str(file_for_write.read(1)) != '':
			file_for_write.seek(0)
			for i in file_for_write:                    # Previous numbers
				list_for_numbering.append(i[0])
			
			number = str(int(list_for_numbering[-1])+1) # Number for write 
			# Writing into a file
			line_write = '\n' + number + ' : ' + data +' : ' + 'WMZ ' + exchange_rate[0].text() + '; '  + 'WME ' + exchange_rate[1].text()+';'
			line_write = line_write.encode('ascii','ignore')
			file_for_write.write(line_write) 
		else:
			# Writing into a file
			line_write = '1' + ' : ' + data +' : ' + 'WMZ ' + exchange_rate[0].text() + '; '  + 'WME ' + exchange_rate[1].text()+';'
			line_write = line_write.encode('ascii','ignore')
			file_for_write.write(line_write)

from grab import Grab
g = Grab()
g.go('http://wmo.com.ua/')
buy = []
sell = []
# ----Parser----
buy.append(g.doc.select("//div[@id='home_courses_buy']/div[@class ='home_courses_item home_courses_wmz']/span"))
buy.append(g.doc.select("//div[@id='home_courses_buy']/div[@class='home_courses_item home_courses_wme']/span"))

sell.append(g.doc.select("//div[@id='home_courses_sell']/div[@class='home_courses_item home_courses_wmz']/span"))
sell.append(g.doc.select("//div[@id='home_courses_sell']/div[@class='home_courses_item home_courses_wme']/span"))
# </----Parser---->
			

write_to_file('buy.txt', buy)		
write_to_file('sell.txt', sell)	

