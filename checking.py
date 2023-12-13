"""CODE TO PERFORM GOOGLE SEARCH IN PYTHON"""

try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
 
# to search
query = "ethopian holidays in each month of the year"
 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)