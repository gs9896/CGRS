-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 18, 2019 at 08:13 AM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cgrsdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admindetail`
--

CREATE TABLE `admindetail` (
  `admin_id` int(15) NOT NULL,
  `name` char(50) NOT NULL,
  `password` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admindetail`
--

INSERT INTO `admindetail` (`admin_id`, `name`, `password`) VALUES
(12981, 'Rajesh', 150283);

-- --------------------------------------------------------

--
-- Table structure for table `complaintdb`
--

CREATE TABLE `complaintdb` (
  `RollNo` int(50) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `empname` varchar(50) NOT NULL DEFAULT 'None',
  `Date` date NOT NULL,
  `complaintId` int(20) NOT NULL,
  `Complaint` text NOT NULL,
  `category` varchar(30) NOT NULL,
  `Status` varchar(20) DEFAULT 'Not Yet',
  `Action` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaintdb`
--

INSERT INTO `complaintdb` (`RollNo`, `Name`, `empname`, `Date`, `complaintId`, `Complaint`, `category`, `Status`, `Action`) VALUES
(2817001, 'Rahul', 'Mr. Vinesh', '2019-08-13', 1, 'All the complaints related to \nAcademics will be posted \nhere...\n', 'Academic (Lectures)', 'Not Yet', ''),
(2817001, 'Rahul', 'Mr. Ajay', '2019-08-13', 2, 'All the complaints regarding \nTraining and Placement will\nbe discussed here...\n', 'Training & Placement cell', 'Processing', '2019-08-14:\nyour request is under process-\ning\n2019-08-14:\nyour problem will be solved \nshortly :)\n'),
(2817002, 'Vijay', 'Mr. Vinesh', '2019-08-13', 3, 'All the complaints regarding \nHostel will\nbe discussed here...\n', 'Hostel', 'Not Yet', ''),
(2817002, 'Vijay', 'Mr. Prakash', '2019-08-13', 4, 'All the complaints related \nTransport will\nbe posted here...\n', 'Transport', 'Not Yet', ''),
(2817003, 'Ashish', 'Mr. Rupesh', '2019-08-13', 6, 'All the complaints regarding \nBooks service in library will\nbe discussed here...\n', 'library', 'Not Yet', ''),
(2817004, 'Parul', 'Mr. Prakash', '2019-08-13', 7, 'All the complaints regarding \nCanteen will be discussed \nhere...\n', 'Canteen', 'Not Yet', ''),
(2817004, 'Parul', 'Mr. Ajay', '2019-08-13', 8, 'If you have any another kind of \nproblem too\nyou can also post it here....\n\n', 'others', 'Processing', '2019-08-13:\nunder process...\n'),
(2817001, 'Rahul', 'Mr. Ajay', '2019-08-15', 9, 'complaint .....\n:)\n', 'Canteen', 'Not Yet', '');

-- --------------------------------------------------------

--
-- Table structure for table `empdetails`
--

CREATE TABLE `empdetails` (
  `empid` int(20) NOT NULL,
  `empname` varchar(50) NOT NULL,
  `password` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `empdetails`
--

INSERT INTO `empdetails` (`empid`, `empname`, `password`) VALUES
(1700, 'Mr. Rupesh', 110182),
(1701, 'Mr. Ajay', 1283),
(1702, 'Mr. Vinesh', 3581),
(1703, 'Mr. Prakash', 9280);

-- --------------------------------------------------------

--
-- Stand-in structure for view `relational`
-- (See below for the actual view)
--
CREATE TABLE `relational` (
);

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE `userdetails` (
  `Roll_No` int(15) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `password` int(20) NOT NULL,
  `Department` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`Roll_No`, `Name`, `password`, `Department`, `Email`) VALUES
(2817001, 'Rahul', 1198, 'CSE', 'rahul@gmail.com'),
(2817002, 'Vijay', 2199, 'CIVIL', 'vijay@gmail.com'),
(2817003, 'Ashish', 5398, 'IT', 'ashish@gmail.com'),
(2817004, 'Parul', 12497, 'CSE', 'parul@gmail.com');

-- --------------------------------------------------------

--
-- Structure for view `relational`
--
DROP TABLE IF EXISTS `relational`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `relational`  AS  select `empdetails`.`name` AS `name`,`empdetails`.`address` AS `address`,`empdetails`.`city` AS `city`,`empdetails`.`phn` AS `phn` from `empdetails` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admindetail`
--
ALTER TABLE `admindetail`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `complaintdb`
--
ALTER TABLE `complaintdb`
  ADD PRIMARY KEY (`complaintId`);

--
-- Indexes for table `empdetails`
--
ALTER TABLE `empdetails`
  ADD PRIMARY KEY (`empid`);

--
-- Indexes for table `userdetails`
--
ALTER TABLE `userdetails`
  ADD PRIMARY KEY (`Roll_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `complaintdb`
--
ALTER TABLE `complaintdb`
  MODIFY `complaintId` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `userdetails`
--
ALTER TABLE `userdetails`
  MODIFY `Roll_No` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2817007;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
