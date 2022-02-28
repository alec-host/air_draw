====================================================================================
CREATE THE FOLLOWING SCHEMAS
====================================================================================

CREATE TABLE `tbl_customer_entries` (
	`_Id` INT(10) NOT NULL AUTO_INCREMENT,
	`company_name` VARCHAR(25) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`company_identifier` VARCHAR(25) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`name` VARCHAR(25) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`msisdn` VARCHAR(15) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`email` VARCHAR(25) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`ticket_no` VARCHAR(12) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`amount` DOUBLE(7,2) NULL DEFAULT NULL,
	`package` VARCHAR(50) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`tier` VARCHAR(50) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`date_created` DATETIME NULL DEFAULT NULL,
	`date_modified` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
	`is_archived` INT(1) NULL DEFAULT '0',
	PRIMARY KEY (`_Id`) USING BTREE,
	INDEX `IsArchive` (`is_archived`) USING BTREE,
	INDEX `CustomerMSISDN` (`msisdn`) USING BTREE,
	INDEX `CustomerEmail` (`email`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0;

===================================================================================

CREATE TABLE `tbl_draw_entries` (
	`_id` INT(10) NOT NULL AUTO_INCREMENT,
	`msisdn` VARCHAR(15) NOT NULL COLLATE 'latin1_swedish_ci',
	`name` VARCHAR(100) NOT NULL COLLATE 'latin1_swedish_ci',
	`ticket_no` VARCHAR(15) NOT NULL COLLATE 'latin1_swedish_ci',
	`tier` INT(1) NOT NULL DEFAULT '0',
	PRIMARY KEY (`_id`) USING BTREE,
	INDEX `tier` (`tier`) USING BTREE,
	INDEX `ticket_no` (`ticket_no`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0;

===================================================================================

CREATE TABLE `tbl_draw_manifest` (
	`_id` INT(10) NOT NULL AUTO_INCREMENT,
	`period_in_months` VARCHAR(20) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`package` VARCHAR(20) NULL DEFAULT NULL COLLATE 'latin1_swedish_ci',
	`cost` DOUBLE(7,2) NULL DEFAULT '0.00',
	`entries` INT(3) NULL DEFAULT '0',
	`is_deleted` INT(1) NULL DEFAULT '0',
	PRIMARY KEY (`_id`) USING BTREE,
	INDEX `period_in_months` (`period_in_months`) USING BTREE,
	INDEX `cost` (`cost`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0;

===================================================================================

CREATE TABLE `tbl_draw_winners` (
	`_id` INT(10) NOT NULL AUTO_INCREMENT,
	`msisdn` VARCHAR(15) NOT NULL COLLATE 'latin1_swedish_ci',
	`name` VARCHAR(100) NOT NULL COLLATE 'latin1_swedish_ci',
	`ticket_no` VARCHAR(15) NOT NULL COLLATE 'latin1_swedish_ci',
	`tier` INT(1) NOT NULL DEFAULT '0',
	PRIMARY KEY (`_id`) USING BTREE,
	INDEX `tier` (`tier`) USING BTREE,
	INDEX `ticket_no` (`ticket_no`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0;

====================================================================================
CREATE TRIGGER
====================================================================================

CREATE DEFINER=`root`@`localhost` TRIGGER `tbl_customer_entries_after_insert` AFTER INSERT ON `tbl_customer_entries` FOR EACH ROW BEGIN
	IF(NEW.msisdn IS not NULL && NEW.ticket_no IS not NULL) THEN
		INSERT INTO `tbl_draw_entries` (`msisdn`,`name`,`ticket_no`,`tier`) VALUES (NEW.msisdn,NEW.name,NEW.ticket_no,NEW.tier);
	END IF;
END