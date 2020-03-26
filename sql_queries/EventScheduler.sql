USE `gpdataengineer`;
DROP EVENT IF EXISTS `calculate average margin hourly`;
CREATE
    EVENT `calculate average margin hourly`
    ON SCHEDULE EVERY 1 HOUR STARTS '2020-03-25 00:00:00'
    ON COMPLETION PRESERVE
    DO CALL hourly_margin_aggregation();