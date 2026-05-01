from data_logger import log_result

log_result(
    product_name="Coupling Nut",
    predicted_class="Defective",
    confidence=0.92,
    image_path="data/raw/test.jpg",
    sensor_trigger="YES",
    action_taken="SORT",
    defect_type="Missing Nut",
    remarks="Initial test entry"
)