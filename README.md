# Defect/Service Request Ideas

A pair of potential ideas for service request analysis.

The first of these, index.html, is a very primitive access to a locally stored database. All it is doing is storing and displaying defects. Clearly such tools already exist and are much better done. However, wanted to experiment with some basic html, db operations, and css. The db itself is forked from professorf/IndexedDB on github and repurposed - it was originally a guestbook operation. I modified it to be something more familiar to us, altered some of the formatting, and added some basic css information.

In a real world operation, HTNML, JavaScript, etc. will likely be necessary to display the data. However, it would be very useful to be able to do some advanced queries on the fly. To give an example of how that might work I created a basic Python script which reads an Excel file of service requests and via a REST API interface preps and displays a chart showing defect trends - returning such charts in a browser (as the screenshots show). In the real world the script would be a lot more involved. Instead of reading an Excel spreadsheet it would likely perform a series of queries to gather the needed data and the REST API could be used to provide significant slicing capability on the fly.

