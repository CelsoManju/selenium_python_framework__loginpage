# Run pytest with HTML report generation
pytest LoginTests.py --html="report.html" --self-contained-html

# Define the items to copy
$items_to_copy = @('report.html', 'automation.log', 'verifyLoginSuccessful_true.png', 'verifyLoginSuccessful_false.png', 'verifyLoginfailed_false.png', 'verifyLoginfailed_true.png')

# Define the result directory
$result_dir = ".\result"

# Create the result directory if it doesn't exist
if (-not (Test-Path $result_dir)) {
    mkdir $result_dir
}

# Copy the items to the result directory
foreach ($item in $items_to_copy) {
    if (Test-Path $item) {
        Copy-Item $item -Destination $result_dir
    } else {
        Write-Host "Warning: $item not found and will not be copied."
    }
}