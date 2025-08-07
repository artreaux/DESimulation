INSERT INTO Analytical_Business_Table 
(
    DATE_BOOKED, 
    ORIGIN, 
    DESTINATION, 
    ORDER_REF, 
    TICKET_NO, 
    SEATNO, 
    DATE_REDEEMED, 
    EMAIL, 
    MOBILENO, 
    FARE, 
    CONVENIENCE_FEE, 
    DISCOUNT, 
    DEPARTURE_DATE, 
    DEPARTURE_TIME, 
    BUS_TYPE, 
    NUMBER_OF_VOUCHERS_BOOKED, 
    BOOK_DT, 
    BOOK_TM, 
    DEPARTURE_DAY, 
    BOOKING_INFO, 
    VOUCHER, 
    ROUTE, 
    TRIP_ID, 
    TRIP_ID_DAY, 
    REDEEMED_FLAG
) 
SELECT 
	DATE_BOOKED, 
    ORIGIN, 
    DESTINATION, 
    ORDER_REF, 
    TICKET_NO, 
    SEATNO, 
CASE 
    WHEN DATE_REDEEMED = 'UNREDEEMED' OR DATE_REDEEMED = 'Unredeemed' THEN NULL
    ELSE DATE_REDEEMED 
END AS DATE_REDEEMED,
    EMAIL, 
    MOBILENO, 
    FARE, 
    CONVENIENCE_FEE, 
    DISCOUNT, 
	DEPARTURE_DATE, 
    DEPARTURE_TIME, 
    BUS_TYPE, 
    NUMBER_OF_VOUCHERS_BOOKED, 
    -- Extract only the date part from DATE_BOOKED
    DATE(
        CASE 
            WHEN DATE_BOOKED REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4} [0-9]{1,2}:[0-9]{1,2}$' THEN 
                STR_TO_DATE(DATE_BOOKED, '%m/%d/%Y %H:%i') 
            WHEN DATE_BOOKED REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4} [0-9]{1,2}:[0-9]{1,2}$' THEN 
                STR_TO_DATE(DATE_BOOKED, '%d/%m/%Y %H:%i') 
            WHEN DATE_BOOKED REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$' THEN 
                STR_TO_DATE(DATE_BOOKED, '%Y-%m-%d %H:%i:%s') 
            ELSE NULL 
        END
    ) AS BOOK_DT, 
    -- Extract only the time part
    TIME(
        CASE 
            WHEN DATE_BOOKED REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4} [0-9]{1,2}:[0-9]{1,2}$' THEN 
                STR_TO_DATE(DATE_BOOKED, '%m/%d/%Y %H:%i') 
            WHEN DATE_BOOKED REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4} [0-9]{1,2}:[0-9]{1,2}$' THEN 
                STR_TO_DATE(DATE_BOOKED, '%d/%m/%Y %H:%i') 
            WHEN DATE_BOOKED REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$' THEN 
                STR_TO_DATE(DATE_BOOKED, '%Y-%m-%d %H:%i:%s') 
            ELSE NULL 
        END
    ) AS BOOK_TM, 
    LEFT(DAYNAME(DEPARTURE_DATE), 3) AS DEPARTURE_DAY, 
    CASE 
        WHEN ORDER_REF LIKE '%OFF%' THEN 'Offline' 
        ELSE 'Online' 
    END AS BOOKING_INFO,  
    CASE
        WHEN LEFT(NUMBER_OF_VOUCHERS_BOOKED, 1) = '1' THEN 'Individual'
        WHEN LEFT(NUMBER_OF_VOUCHERS_BOOKED, 1) = '2' THEN 'Pair'
        WHEN CAST(LEFT(NUMBER_OF_VOUCHERS_BOOKED, 1) AS UNSIGNED) >= 3 THEN 'Group'
        ELSE NULL
    END AS VOUCHER, 
    CONCAT(ORIGIN, ' to ', DESTINATION) AS ROUTE, 
    CONCAT(
        UPPER(LEFT(ORIGIN, 3)), 
        '-', 
        UPPER(LEFT(DESTINATION, 3)), 
        '-', 
        UPPER(LEFT(DAYNAME(DEPARTURE_DATE), 3)), 
        '-', 
        IFNULL(LEFT(DEPARTURE_TIME, 2), '00')
    ) AS TRIP_ID, 
    CONCAT(
        UPPER(LEFT(ORIGIN, 3)), 
        '-', 
        UPPER(LEFT(DESTINATION, 3)), 
        '-', 
        UPPER(LEFT(DAYNAME(DEPARTURE_DATE), 3))
    ) AS TRIP_ID_DAY, 
    CASE 
        WHEN DATE_REDEEMED IS NULL OR DATE_REDEEMED = 'Unredeemed' THEN 'N'
        ELSE 'Y'
    END AS REDEEMED_FLAG
FROM staging_table;