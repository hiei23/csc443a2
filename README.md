# Big Data - Map Reduce Problems

### 1. Inverted index ###

#### Mapper Input ####
	The input is a 2 element list: [document_id, text], where document_id is a string representing a document identifier and text is a string representing the text of the document. The document text may have words in upper or lower case and may contain punctuation. You should treat each token as if it was a valid word; that is, you can just use value.split() to tokenize the string.

#### Reducer Output ####
		The output should be a (word, document ID list) tuple where word is a String and document ID list is a list of Strings.

### 2. Join ###
**Query**:

		SELECT *
		FROM Orders, LineItem
		WHERE Order.order_id = LineItem.order_id

#### Mapper Input ####
	Each input record is a list of strings representing a tuple in the database. Each list element corresponds to a different attribute of the table

	The first item (index 0) in each record is a string that identifies the table the record originates from. This field has two possible values:
		"line_item" indicates that the record is a line item.
		"order" indicates that the record is an order.

	The second element (index 1) in each record is the order_id.
	LineItem records have 17 attributes including the identifier string.
	Order records have 10 elements including the identifier string.

### Reducer Output:
		The output should be a joined record: a single list of length 27 that contains the attributes from the order record followed by the fields from the line item record. Each list element should be a string.

### 3. Symmetric friends ###

	Generate a count of all true friends per person.

#### Mapper Input ####
		Each input record is a 2-element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends.

#### Reducer Output ####
		The output should be a pair (person, friend_count) where person is a string and friend_count is an integer indicating the number of true friends associated with this person.

### 4. Cleaning DNA sequences ###

#### Mapper Input ####
		Each input record is a 2-element list [sequence id, nucleotides] where sequence id is a string representing a unique identifier for the sequence and nucleotides is a string representing a sequence of nucleotides.

#### Reducer Output ####
		The output from the reduce function should be the unique trimmed nucleotide strings.
