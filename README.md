# anomaly-detection
# Author: Chris Munson
# Version: 1.0

Python code to read input of transaction data from an e-commerce site,
flag any anomalous transactions, as defined by being over (mean+3*std) and store them in an output file.

##File structure:
anomaly-detection
├── README.md 

├── run.sh

├── src

│   └── streaming.py

│   └── read_batch.py

│   └── read_funcs.py

│   └── calculate.py

├── log_input

│   └── batch_log.json

│   └── stream_log.json

├── log_output

|   └── flagged_purchases.json

├── insight_testsuite

    └── run_tests.sh
	
    └── tests
	
        └── test_1
		
        |   ├── log_input
		
        |   │   └── batch_log.json
		
        |   │   └── stream_log.json
		
        |   |__ log_output
		
        |   │   └── flagged_purchases.json
		

##Usage: 

Running run.sh will call streaming.py with arguments for the input and output files

##Dependencies:

	-re
	
	-json
	
	-sys
	
	-collections
	
	-math

##Known bugs: 

	-Whitespace at the end of the stream_log.json will crash the program
	
	-Corrupted or incorrectly formatted json files will crash the program

##Wishlist of features for future revisions:

	-Fixing above bugs (PRIORITY)
	
	-Storing purchase lists by user to file and only loading them during calculations to reduce memory overhead
	
	-Set up error handling so that bugs will throw errors rather than crash
	
	-Clean up code
	
	-Eliminate redundancies and streamline execution
	
	-Inspect creation of initial mean and stds to see if there are further optimizations that can be done
	