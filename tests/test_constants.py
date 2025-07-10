"""
This is a simple set of tests to make sure constants are properly defined
"""

import pytest

# Import the module
from data_processing import constants

class TestConstants:
    """Tests for our constants module"""
    def test_fiscal_year_defined(self):
        """
        Check that the fiscal year is defined.
        """
        assert hasattr(constants, 'FISCAL_YEAR')
        assert isinstance(constants.FISCAL_YEAR, str)
        # Should be a 4-digit year
        assert len(constants.FISCAL_YEAR) == 4
        assert constants.FISCAL_YEAR.isdigit()
    
    def test_agency_display_names(self):
        """
        Test the agency display name mapping.
        """
        assert hasattr(constants, 'AGENCY_DISPLAY_NAMES')
        assert isinstance(constants.AGENCY_DISPLAY_NAMES, dict)
        assert len(constants.AGENCY_DISPLAY_NAMES) > 0
        
        assert 'AGRICULTURE, DEPARTMENT OF' in constants.AGENCY_DISPLAY_NAMES
        assert constants.AGENCY_DISPLAY_NAMES['AGRICULTURE, DEPARTMENT OF'] == 'Department of Agriculture'
    
    def test_assistance_type_display_names(self):
        """
        Test the assistance type display name mapping.
        """
        assert hasattr(constants, 'ASSISTANCE_TYPE_DISPLAY_NAMES')
        assert isinstance(constants.ASSISTANCE_TYPE_DISPLAY_NAMES, dict)
        assert len(constants.ASSISTANCE_TYPE_DISPLAY_NAMES) > 0
        
        
        assert 'FORMULA GRANTS' in constants.ASSISTANCE_TYPE_DISPLAY_NAMES
        assert constants.ASSISTANCE_TYPE_DISPLAY_NAMES['FORMULA GRANTS'] == 'Formula Grants'
    
    def test_cfo_act_agency_names(self):
        """
        Test the CFO Act agency list.
        """
        assert hasattr(constants, 'CFO_ACT_AGENCY_NAMES')
        assert isinstance(constants.CFO_ACT_AGENCY_NAMES, list)
        assert len(constants.CFO_ACT_AGENCY_NAMES) > 0
        
        # There should be 24 CFO Act agencies
        assert len(constants.CFO_ACT_AGENCY_NAMES) == 24
        
        assert 'Department of Agriculture' in constants.CFO_ACT_AGENCY_NAMES
        assert 'Department of Defense' in constants.CFO_ACT_AGENCY_NAMES
        assert 'Department of the Treasury' in constants.CFO_ACT_AGENCY_NAMES
    
    def test_program_type_mapping(self):
        """
        Test the program type display mapping.
        """
        assert hasattr(constants, 'PROGRAM_TYPE_MAPPING')
        assert isinstance(constants.PROGRAM_TYPE_MAPPING, dict)
        assert len(constants.PROGRAM_TYPE_MAPPING) > 0
        
        # Check all entries
        assert 'tax_expenditure' in constants.PROGRAM_TYPE_MAPPING
        assert constants.PROGRAM_TYPE_MAPPING['tax_expenditure'] == 'Tax Expenditures'
        
        assert 'assistance_listing' in constants.PROGRAM_TYPE_MAPPING
        assert constants.PROGRAM_TYPE_MAPPING['assistance_listing'] == 'Federal Financial Assistance'
        
        assert 'interest' in constants.PROGRAM_TYPE_MAPPING
        assert constants.PROGRAM_TYPE_MAPPING['interest'] == 'Interest on the Public Debt'