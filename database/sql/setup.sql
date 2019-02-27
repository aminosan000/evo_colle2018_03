-- 名刺テーブル作成
CREATE TABLE evo_db.business_card (
    card_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32),
    company VARCHAR(32),
    tel VARCHAR(16),
    mail VARCHAR(32),
    user_id VARCHAR(32)
    );

-- ユーザテーブル作成
CREATE TABLE evo_db.user (
    user_id VARCHAR(32) PRIMARY KEY,
    password VARCHAR(256)
    );

-- ユーザデータ登録
INSERT INTO evo_db.user (user_id, password) VALUES
    ('user1', SHA2('user1', 256)),
    ('user2', SHA2('user2', 256));
