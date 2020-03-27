USE `gpdataengineer`;
DROP procedure IF EXISTS `hourly_margin_aggregation`;

DELIMITER $$
USE `gpdataengineer`$$
CREATE DEFINER=`root`@`%` PROCEDURE `hourly_margin_aggregation`()
BEGIN
	IF (select COUNT(*) from gpdataengineer.AvgMarginHourly)<1 THEN
        INSERT INTO gpdataengineer.AvgMarginHourly 
		(time, date, margin_avg, payment_type, ad_type)
		SELECT hour(time_created_at), date_created_at, 
			avg((price-payment_cost)/price) as margin_avg, 
			payment_type, ad_type 
		FROM gpdataengineer.Classifieds
		GROUP BY payment_type, ad_type, hour(time_created_at), date_created_at;
	ELSEIF (select COUNT(*) from gpdataengineer.AvgMarginHourly)>0 THEN
		INSERT INTO gpdataengineer.AvgMarginHourly 
		(time, date, margin_avg, payment_type, ad_type)
		SELECT hour(time_created_at), date_created_at, 
			avg((price-payment_cost)/price) as margin_avg, 
			payment_type, ad_type 
		FROM gpdataengineer.Classifieds
			WHERE date_created_at >=(SELECT date FROM gpdataengineer.AvgMarginHourly order by date desc, time desc limit 1)
			and hour(time_created_at) >(SELECT time FROM gpdataengineer.AvgMarginHourly order by date desc, time desc limit 1)
		GROUP BY payment_type, ad_type, hour(time_created_at), date_created_at;
    END IF;
END$$

DELIMITER ;