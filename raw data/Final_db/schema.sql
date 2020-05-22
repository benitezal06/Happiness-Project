--Drop Table 
DROP TABLE happiness

--Create a new table
CREATE TABLE happiness(
	Country varchar Not null,
	Data_Year varchar Not null,
	Happiness_rank varchar Not null,
	Happiness_score varchar Not null,
	Life_Expectancy varchar not null,
	Population varchar not null
)
--Select everything from the table housing.
SELECT *
FROM happiness