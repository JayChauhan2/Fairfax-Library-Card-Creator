# Virginia Library Card Creator

Automated script to create library cards at top Virginia libraries for instant access to Libby and online reading platforms.

## Overview

This Python script automates the library card registration process for Virginia's public library systems, giving you immediate access to digital resources like Libby, OverDrive, and online reading platforms.

## Prerequisites

- Python 3.7+
- Chrome browser installed
- ChromeDriver (matching your Chrome version)

## Installation

1. Install required dependencies:
```bash
pip install selenium
```

2. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Download version matching your Chrome browser
   - Add to your system PATH or place in project directory

## Usage

```bash
python library_card_creator.py
```

The script will:
1. Open Fairfax County Public Library registration page
2. Fill out the registration form with generated credentials
3. Submit and retrieve your new library card number
4. Display username and password for login

### Output

```
New page loaded!
user: [Your Library Card Number]
password: [Your Generated Password]
```

## Supported Libraries

Currently configured for:
- **Fairfax County Public Library** (City of Fairfax Regional Library)

### Top 5 Popular Virginia Library Systems

To expand to other major Virginia libraries, modify the URL and form fields:

1. **Fairfax County Public Library** (FCPL) - Currently implemented
2. **Arlington Public Library** 
3. **Richmond Public Library**
4. **Virginia Beach Public Library**
5. **Henrico County Public Library**

## Configuration

Edit these variables to customize your registration:

```python
# Library branch
select.select_by_visible_text("City of Fairfax Regional Library")

# Zip code (must be valid for library system)
zip_code.send_keys("23059")

# Birth date (must meet age requirements)
driver.find_element(By.NAME, "txtBirthdatemm").send_keys("09")
driver.find_element(By.NAME, "txtBirthdatedd").send_keys("30")
driver.find_element(By.NAME, "txtBirthdateyyyy").send_keys("2008")

# Address (must be in library service area)
driver.find_element(By.NAME, "txtStreet1").send_keys("11600 Herrick Ln")

# Email
driver.find_element(By.NAME, "txtEmail").send_keys("your-email@example.com")
```

## Using Your Library Card

Once you have your credentials:

1. **Libby App**:
   - Download Libby (iOS/Android)
   - Search for your library
   - Sign in with card number and password
   - Start borrowing ebooks and audiobooks

2. **Online Portal**:
   - Visit library website
   - Log in with credentials
   - Access digital collections

## Important Notes

⚠️ **Eligibility Requirements**:
- Must reside in or be eligible for library service area
- Age requirements vary by library system
- Some libraries require address verification

⚠️ **Terms of Service**:
- Only create accounts you're eligible for
- Respect library policies and usage limits
- One account per person per library system

⚠️ **Temporary Cards**:
- Some libraries issue temporary cards requiring in-person verification
- Digital access may be limited until full verification

## Troubleshooting

**ChromeDriver version mismatch**:
```bash
# Check Chrome version: chrome://version
# Download matching ChromeDriver version
```

**Element not found errors**:
- Library website may have updated their forms
- Check element names/IDs in browser inspector
- Update selectors in script

**Registration fails**:
- Verify zip code matches library service area
- Ensure address is valid and in service area
- Check age meets library requirements

## Legal & Ethical Use

This tool is for:
- ✅ Residents eligible for library cards
- ✅ Automating tedious form-filling
- ✅ Accessing free public resources

Not for:
- ❌ Creating fraudulent accounts
- ❌ Circumventing eligibility requirements
- ❌ Violating library terms of service

## License

This script is provided as-is for educational purposes. Users are responsible for complying with all applicable library policies and terms of service.

## Contributing

To add support for additional Virginia libraries:
1. Inspect the registration form for the target library
2. Update URL and form field selectors
3. Test thoroughly
4. Submit pull request

## Resources

- [Fairfax County Public Library](https://www.fairfaxcounty.gov/library/)
- [Libby App](https://libbyapp.com/)
- [Virginia Public Libraries](https://www.lva.virginia.gov/public/vpl/)
