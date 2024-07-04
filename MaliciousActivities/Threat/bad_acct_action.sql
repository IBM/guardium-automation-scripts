drop procedure move_to_platinum;
CREATE PROCEDURE move_to_platinum (IN user_id VARCHAR(50)) UPDATE ACCOUNT_GROUPS SET GROUP_NAME='PLATINUM';