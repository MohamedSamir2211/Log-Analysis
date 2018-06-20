# Log Analysis

The project is a internal reporting tool that use information from database to discover what kind of articles the site's readers like.

### The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles.
  * The log table includes one entry for each time a user has accessed the site indicates whether the request succeeded or failed.
 
### The reports View used in this project:
  *  **reports**  is used to help to answer the first two questions  so it contian articles  and it's views , query of this view:
      ```
      create view reports as 
	  (
	  select articles.slug, count(log.path) as views 
	  from articles left join log 
	  on slug = substring(path from 10) 
	  group by slug 
	  );
      ```

### The project consist of Four functions:
  * The **execute_query()**          Function Used To Execute Different Queries.
  * The **print_top_articles()**     Function Used To Prints out the top 3 articles of all time.
  * The **print_top_authors()**      Function Used To Prints a list of authors ranked by article views.
  * The **print_errors_over_one()**  Function Used To Prints out the days where more than 1% errors.
  

  
  

### How it works:
  1. you should install python3 from  [here](https://www.python.org/downloads/).
  2. You should have the following :
  1. **vagrant**   installed on your computer download it from [here](https://www.vagrantup.com/downloads.html).
  2. **Virual Box**  installed on you computer downlad it from   [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)  **Hint** your virtualbox must be old verison 5.1.  .. Newer versions do not work with the current release of Vagrant.
  3. Next, download the data here.  The file  newsdata.sql should be inside the vagrant directory.  [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840)
  4.  To  execute sql queries of newsdata.sql , cd into the vagrant directory and use the command **psql -d news -f newsdata.sql**.
  4. Next  cd to the project location and run **python newsdb.py**.
