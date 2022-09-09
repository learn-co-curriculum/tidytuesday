
# LEGO sets

The data this week comes from [rebrickable](https://rebrickable.com/downloads/) courtesy of [Georgios Karamanis](https://github.com/rfordatascience/tidytuesday/issues/455).

> The LEGO Parts/Sets/Colors and Inventories of every official LEGO set in the Rebrickable database is available for download as csv files here. These files are automatically updated daily. If you need more details, you can use the API which provides real-time data, but has rate limits that prevent bulk downloading of data.



### 


### Data Dictionary

# `inventories.csv.gz`

|variable |class     |description |
|:--------|:---------|:-----------|
|id       |double    |variable    |
|version  |double    |variable    |
|set_num  |character |variable    |

# `inventory_sets.csv.gz`

|variable     |class     |description |
|:------------|:---------|:-----------|
|inventory_id |double    |variable    |
|set_num      |character |variable    |
|quantity     |double    |variable    |

# `sets.csv.gz`

|variable  |class     |description |
|:---------|:---------|:-----------|
|set_num   |character |variable    |
|name      |character |variable    |
|year      |double    |variable    |
|theme_id  |double    |variable    |
|num_parts |double    |variable    |
|img_url   |character |variable    |

### 

