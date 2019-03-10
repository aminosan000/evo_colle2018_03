-- 名刺テーブル作成
CREATE TABLE evo_db.business_card (
    card_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32),
    company VARCHAR(32),
    tel VARCHAR(16),
    mail VARCHAR(32)
    );
