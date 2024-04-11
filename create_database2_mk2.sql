CREATE DATABASE IF NOT EXISTS assignment5_datapipeline_mk2;
USE assignment5_datapipeline_mk2;

-- Create Customer1 table
CREATE TABLE IF NOT EXISTS customer2_data (
    `Customer ID` VARCHAR(255) PRIMARY KEY,
    `Last Used Platform` VARCHAR(255),
    `Is Blocked` VARCHAR(255),
    `Created At` VARCHAR(255),
    `Language` VARCHAR(255),
    `Outstanding Amount` DECIMAL(10, 2),
    `Loyalty Points` VARCHAR(255)
);

-- Create deliveries2 table
CREATE TABLE IF NOT EXISTS deliveries2_data (
    `Task_ID` VARCHAR(255) PRIMARY KEY,
    `Order_ID` VARCHAR(255),
    `Relationship` VARCHAR(255),
    `Team_Name` VARCHAR(255),
    `Task_Type` DECIMAL(10, 2),
    `Agent_ID` VARCHAR(255),
    `Agent_Name` VARCHAR(255),
    `Distance_m` VARCHAR(255),
    `Total_Time_Taken_min` DATE,
    `Task_Status` DECIMAL(10, 2),
    `Ref_Images` VARCHAR(255),
    `Rating` VARCHAR(255),
    `Review` VARCHAR(255),
    `Latitude` VARCHAR(255),
    `Longitude` VARCHAR(255),
    `Promo_Applied` VARCHAR(255), 
    `Custom_Template_ID` VARCHAR(255), 
    `Task_Details_QTY` VARCHAR(255),
    `Task_Details_AMOUNT` VARCHAR(255), 
    `Special_Instructions` VARCHAR(255), 
    `Tip` VARCHAR(255),
    `Delivery_Charges` VARCHAR(255), 
    `Discount` VARCHAR(255), 
    `Subtotal` VARCHAR(255), 
    `Payment_Type` VARCHAR(255),
    `Task_Category` VARCHAR(255), 
    `Earning` VARCHAR(255), 
    `Pricing` VARCHAR(255) 
);

-- Create order2 table
CREATE TABLE IF NOT EXISTS orders2_data (
    `Order ID` VARCHAR(255) PRIMARY KEY, 
    `Order Status` VARCHAR(255), 
    `Category Name` VARCHAR(255), 
    `SKU` VARCHAR(255), 
    `Quantity` VARCHAR(255),
    `Unit Price` DECIMAL(10, 2), 
    `Cost Price` DECIMAL(10, 2), 
    `Total Cost Price` DECIMAL(10, 2), 
    `Total Price` DECIMAL(10, 2),
    `Order Total` DECIMAL(10, 2), 
    `Sub Total` DECIMAL(10, 2), 
    `Tax` DECIMAL(10, 2), 
    `Delivery Charge` DECIMAL(10, 2), 
    `Tip` DECIMAL(10, 2), 
    `Discount` DECIMAL(10, 2),
    `Remaining Balance` DECIMAL(10, 2), 
    `Payment Method` VARCHAR(255), 
    `Additional Charge` DECIMAL(10, 2),
    `Taxable Amount` DECIMAL(10, 2), 
    `Transaction ID` VARCHAR(255), 
    `Currency Symbol` VARCHAR(255), 
    `Customer_ID` VARCHAR(255),
    `Merchant ID` VARCHAR(255), 
    `Distance_in_km` DECIMAL(10, 2), 
    `Order Time` DATE, 
    `Pickup Time` DATE,
    `Delivery Time` DATE, 
    `Order Preparation Time` DATE, 
    -- `Debt Amount` DECIMAL(10, 2),
    `Redeemed Loyalty Points` DECIMAL(10, 2), 
    `Consumed Loyalty Points` DECIMAL(10, 2), 
    `Flat Discount` DECIMAL(10, 2),
    `Checkout Template Name` VARCHAR(255), 
    `Checkout Template Value` DECIMAL(10, 2),
    -- `Last Used Platform` VARCHAR(255),
    -- `Is Blocked` VARCHAR(255),
    -- `Created At` VARCHAR(255),
    `Language` VARCHAR(255),
    `Outstanding Amount` DECIMAL(10, 2),
    `Loyalty Points` VARCHAR(255)
);
