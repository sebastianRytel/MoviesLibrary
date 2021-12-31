# MoviesLibrary

# Table of contents
* [General info](#general-info)
* [Technologies](#technologies)

## General info

<details>
    <summary>Click here to see general information about application!</summary>
        <br>
        Movies Library is an web app which allows user to store information about his favourite movies. Search features uses IMBD API for looking information about the movie. 
        The amount of data pulled from IMBD is limited by the API. The API itself is free and is taken from RapidApi hub.
        </br>
        App allows user to perform following actions:
        <ul>
          <li>Search for a movie using search engine. Splitted into three subsearch features:</li>
            <ul>
                <li>Exact search by title (returns only one movie based on exact title, stored in the same way as in IMBD),</li>
                <li>Overall search by title (returns all movies which have similar title),</li>
                <li>Search by IMBD ID (returns only one movie based on IMBD ID, which is unique for each movie).</li>
            </ul>
          <li>Edit movie before saving record to Database. At this point user is able to:
            <ul>
                <li>rate the movie (in a scale 0-5),</li>
                <li>assign predefined tag,</li>
                <li>flag if the movie has been watched or is it on wishlist,</li>
                <li>paste the link to streaming portal, where movie can be found</li>
                <li>write own comments about the film</li>
            </ul>
          <li>Browse, update and delete movies stored in Movie Library</li>
          <li>Search for a particular movie using filter engine with predefined filters</li>
          <li>Create movie tags and store them in Database</li>
          <li>Browse, update and delete tags stored in Tags Library</li>    
</details>

## Technologies

<details>
    <summary>Click here to see the technologies used!</summary>
        <ul>
          <li>Python 3.8.5</li>
          <li>Django 3.2.8</li>          
          <li>HTML 5</li>
          <li>CSS 3</li>
          <li>Docker</li>
          <li>Docker Compose</li>
          <li>Bootstrap</li>
          <li>AWS Elasticbeanstalk</li>
          <li>AWS S3</li>
          <li>AWS RDS</li>
        </ul>
</details>
