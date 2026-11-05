CREATE DATABASE ola_ride_insights;


USE ola_ride_insights;

show tables;

select * from ola_dataset
limit 10 ;


Select Count(*) as Total_records from ola_dataset;

-- SQL Questions

-- 1. Retrieve all successful bookings:

select * from ola_dataset
where Booking_Status = 'success';

-- 2. Find the average ride distance for each vehicle type:

SELECT
    Vehicle_Type,
    ROUND(AVG(Ride_Distance), 2) AS Average_Ride_Distance
FROM ola_dataset
GROUP BY Vehicle_Type
ORDER BY Average_Ride_Distance DESC;

-- Q3. Get the total number of cancelled rides by customers 

SELECT
    COUNT(*) AS Total_Customer_Cancellations
FROM ola_dataset
WHERE Booking_Status = 'Canceled by Customer';

-- Q4. List the top 5 customers who booked the highest number of rides

SELECT
    Customer_ID,
    COUNT(Booking_ID) AS Total_Rides
FROM ola_dataset
GROUP BY Customer_ID
ORDER BY Total_Rides DESC
LIMIT 5;




-- Q5. Get the number of rides cancelled by drivers due to personal and car-related issues

SELECT
    Canceled_Rides_by_Driver,
    COUNT(*) AS Total_Rides
FROM ola_dataset
WHERE Canceled_Rides_by_Driver IS NOT NULL
GROUP BY Canceled_Rides_by_Driver;


-- Q6. Find the maximum and minimum driver ratings for Prime Sedan bookings

SELECT
    MAX(Driver_Ratings) AS Maximum_Driver_Rating,
    MIN(Driver_Ratings) AS Minimum_Driver_Rating
FROM ola_dataset
WHERE Vehicle_Type = 'Prime Sedan';

-- Q7. Retrieve all rides where payment was made using UPI

 SELECT *
FROM ola_dataset
WHERE Payment_Method = 'UPI';

-- Q8. Find the average customer rating per vehicle type

SELECT
    Vehicle_Type,
    ROUND(AVG(Customer_Rating), 2) AS Average_Customer_Rating
FROM ola_dataset
GROUP BY Vehicle_Type
ORDER BY Average_Customer_Rating DESC; 


--  Q9. Calculate the total booking value of rides completed successfully

SELECT
    ROUND(SUM(Booking_Value), 2) AS Total_Successful_Booking_Value
FROM ola_dataset
WHERE Booking_Status = 'Success'; 



-- Q10. List all incomplete rides along with the reason

SELECT
    Incomplete_Rides,
    COUNT(*) AS Total_Rides
FROM ola_dataset
WHERE Incomplete_Rides IS NOT NULL
GROUP BY Incomplete_Rides;




