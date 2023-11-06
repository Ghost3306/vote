-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 10, 2023 at 08:20 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vote`
--

-- --------------------------------------------------------

--
-- Table structure for table `allusers`
--

CREATE TABLE `allusers` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,cd
  `typeuser` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `allusers`
--

INSERT INTO `allusers` (`name`, `email`, `phone`, `age`, `address`, `typeuser`, `password`) VALUES
('Lalit Rajan Rawool', 'lrrawool2503@gmail.com', '9604449928', '20', 'Halwal', 'admin', 'Root'),
('Om Rajan Rawool', 'lrrawool2503@gmail.com', '7878787878', '20', 'Kudal', 'admin', 'root'),
('sdf adc acsc', 'acsc', '08805075031', '20', 'casc', 'admin', 'root'),
('asc cas csac', 'lrrawool2503@gmail.com', '0880507703565', '20', 'csaC', 'admin', 'root'),
('Lalit Rajan Rawool', 'lalit@gmail.com', '9898989898', '20', 'Halwal', 'admin', 'root'),
('vsv vsdv dsvd', 'lalit25@gmail.com', '7855487545', '20', 'dsv', 'admin', 'root'),
('Lalit Rajan Rawool', 'lrrawool2503@gmail.com', '7874554878', '20', 'Halwal', 'admin', 'root'),
('svsv vsdv vsd', 'lalit@gmail.com', '8585858585', '20', 'vsdv', 'admin', 'root'),
('vdv vsd vsd', 'lalit@gmail.com', '', '20', 'Halwal', 'admin', 'root'),
('Lalit Rajan Rawool', 'lalit@gmail.com', '088050770', '20', 'Halwal', 'admin', 'root'),
('vds sdv dcs', 'lalit25@gmail.com', '9856985625', '20', 'dcsc', 'admin', 'root');

-- --------------------------------------------------------

--
-- Table structure for table `bsccs`
--

CREATE TABLE `bsccs` (
  `name` varchar(30) DEFAULT NULL,
  `vote` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `electionslist`
--

CREATE TABLE `electionslist` (
  `elenm` varchar(40) NOT NULL,
  `admin` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `electionslist`
--

INSERT INTO `electionslist` (`elenm`, `admin`) VALUES
('bsccs', '9604449928'),
('Ty', '9604449928');

-- --------------------------------------------------------

--
-- Table structure for table `ty`
--

CREATE TABLE `ty` (
  `name` varchar(30) DEFAULT NULL,
  `vote` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ty`
--

INSERT INTO `ty` (`name`, `vote`) VALUES
('Lalit', NULL),
('Om', NULL),
('Rani', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
