from datetime import datetime
import os, json


class StockMan():
	""" A stock management system"""
	
	def __init__(self):
		self.history = {
		 "index": {},
		 "runtime_log": []
		}

		# print(self.history)

		try :
			with open("stock-management.json", "r") as log :
				# i spent 4 hours here
				history = json.loads(str(log.readline()))
				# print(history)
				self.history = history
				
		except Exception as e :
			# print(e)
			self.update_database()

		# restore states
		self.index = self.history["index"]
		self.runtime_log = self.history["runtime_log"]

	def pad_right(self, _str, pad_val) :
		return _str + " "*(pad_val - len(_str))

	def update_database(self) :
		with open("stock-management.json", "w") as log :
				# log.write(json.dumps(self.history, indent=4))
				log.write(json.dumps(self.history))

	def log(self, transaction_type, stock_quantity, stock_code) :
		dt = str(datetime.now())
		log_entry = "{} {} {} {}".format(dt, transaction_type, stock_quantity, stock_code)
		self.runtime_log.append(log_entry)
		self.update_database()

	def check_index_for_code(self, stock_code):
		return stock_code in self.index.keys()

	def remove_entry(self, stock_code) :
		del self.index[stock_code]

	def push_to_db(self, stock_code, stock_entry):
		self.index[stock_code] = stock_entry

	def add_stock(self, stock_code, item_name):
		stock_code = str(stock_code)
		
		if self.check_index_for_code(stock_code) :
			print("Error: The stock_code must be unique (there's already an entry with such id)")
			# sharp exit
			return 
	 
		stock_entry = {
			"stock_code": stock_code,
			"item_name": item_name,
			"quantity": 0
		}

		# covert the stock_code to str
		self.push_to_db(stock_code, stock_entry)
		self.log("Add", 0, stock_code)
		print("Stock Sucessfully Recorded")
		return True

	def add_stock_quantity(self, stock_code, stock_quantity):
		stock_code = str(stock_code)
		stock_quantity = int(stock_quantity)
		
		if self.check_index_for_code(stock_code) :
			self.index[stock_code]["quantity"] += stock_quantity
			self.log("Recieve", stock_quantity, stock_code)
			print("Sucessfully recorded recieved stock")
		else :
			print("Warning: There's no stock like that in your db")

	def send_stock_quantity(self, stock_code, stock_quantity):
		stock_code = str(stock_code)
		stock_quantity = int(stock_quantity)

		if self.check_index_for_code(stock_code) :
			net_return = self.index[stock_code]["quantity"] - stock_quantity
			if net_return >= 0 :
				self.index[stock_code]["quantity"] = net_return
				self.log("Send", stock_quantity, stock_code)
				print("Sucessfully sent stock")
			else :
				print("Warning: You cannot withdraw more than you have ({})".format(self.index[stock_code]["quantity"]))
		else :
			print("Warning: There's no stock like that in your db")

	def delete_stock(self, stock_code) :
		stock_code = str(stock_code)
		if self.check_index_for_code(stock_code) :
			self.remove_entry(stock_code)
			self.log("Delete", 0, stock_code)
			print("Stock Sucessfully Deleted")
		else :
			print("Warning: There is no entry with such stock_code")

	def display_transactions(self) :
		print(" [ Transactions Made ] \n")
		print("______________________________________________________________________________")
		print(" CODE          | TYPE      | QUANTITY      | DATE          | TIME             |")
		print("_______________|___________|_______________|_______________|__________________|")

		for log in self.runtime_log :
			date, time, transaction_type, stock_quantity, stock_code = log.split(" ")

			# pad the values for better display
			date = self.pad_right(date, 14)
			time = self.pad_right(time, 14)
			transaction_type = self.pad_right(transaction_type, 10)
			stock_quantity = self.pad_right(stock_quantity, 14)
			stock_code = self.pad_right(stock_code, 14)

			print(" {}| {}| {}| {}| {}  |".format(stock_code, transaction_type, stock_quantity, date, time))

	def display_stock_level(self) :
		print("_____________________________________________________|")
		print(" CODE          | Item Name           | QUANTITY      |")
		print("_______________|_____________________|_______________|")

		for stock in self.index.values() :
			item_name = self.pad_right(stock["item_name"], 20)
			quantity = self.pad_right(str(stock["quantity"]), 12)
			stock_code = self.pad_right(stock["stock_code"], 14)

			print(" {}| {}| {}  |".format(stock_code, item_name, quantity))

	def process_input(self, input_str) :
		chunks = input_str.split(" ")
		command = chunks[0]

		if command == "add" :
			stock_code = chunks[1]
			item_name = chunks[2]
			self.add_stock(stock_code, item_name)

		elif command == "delete" :
			stock_code = chunks[1]
			self.delete_stock(stock_code)

		elif command == "receive" :
			stock_code = chunks[1]
			stock_quantity = chunks[2]
			self.add_stock_quantity(stock_code, stock_quantity)

		elif command == "send" :
			stock_code = chunks[1]
			stock_quantity = chunks[2]
			self.send_stock_quantity(stock_code, stock_quantity)

		elif command == "transactions" :
			self.display_transactions()

		elif command == "stocks" :
			self.display_stock_level()

		elif command == "q" :
			exit(0)
		else :
			print("Command not recognized")

if __name__ == '__main__':
	stockman = StockMan()
	print("Stock management system v1.0.0\n")
	print("How to use it ;\n")
	
	print("add [code] [name] - adds i number of name to stock\n")
	print("delete [code] - deletes name from stock\n")
	print("receive [code] [quantity] - adds i number of items to existing stock\n")
	print("send [code] [quantity] - sends i number of items out of stock\n")
	print("stocks - prints current stock items\n")
	print("transactions - displays a list of all transactions\n")
	print("q - exits the program\n")

	while True :
		user_input = input("\n[input]> ")
		stockman.process_input(user_input)
		

	# stockman = StockMan()
	# stockman.add_stock(99, "jeep-2018 version")
	# stockman.add_stock(909, "rice")
	# stockman.add_stock(90889, "rice")
	
	