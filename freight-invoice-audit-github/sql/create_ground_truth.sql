USE freight_audit;
CREATE TABLE IF NOT EXISTS ground_truth (
 id INT AUTO_INCREMENT PRIMARY KEY,
 anomaly_code VARCHAR(50) NOT NULL,
 invoice_id INT NOT NULL,
 anomaly_type VARCHAR(100) NOT NULL,
 expected_value DECIMAL(12,2),
 actual_value DECIMAL(12,2),
 description VARCHAR(500),
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY (invoice_id) REFERENCES freight_invoices(id)
);
