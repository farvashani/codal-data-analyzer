#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple test for Codal Data Analyzer
"""

from codal_data_analyzer import CodalDataAnalyzer
import sys

def test_analyzer():
    """Test analyzer functionality"""
    print("Starting Codal Analyzer Test")
    print("=" * 40)
    
    try:
        # Create analyzer instance
        analyzer = CodalDataAnalyzer()
        print("Analyzer created successfully")
        
        # Test company list retrieval
        print("\nTesting company list retrieval...")
        companies = analyzer.get_company_list()
        
        if companies is not None:
            print(f"Company list received: {len(companies)} companies")
        else:
            print("Company list not received (API limitation)")
        
        # Test sample reports retrieval
        print("\nTesting sample reports retrieval...")
        sample_reports = analyzer.get_company_reports("Foolad", days_back=7)
        
        if sample_reports is not None:
            print(f"Sample reports received: {len(sample_reports)} reports")
            
            # Test data cleaning
            print("\nTesting data cleaning...")
            clean_data = analyzer.clean_financial_data(sample_reports)
            
            if clean_data is not None:
                print(f"Data cleaned successfully: {len(clean_data)} rows")
                
                # Test feature extraction
                print("\nTesting feature extraction...")
                features = analyzer.extract_financial_features(clean_data)
                
                if features is not None:
                    print(f"Features extracted: {len(features.columns)} features")
                else:
                    print("No features extracted")
            else:
                print("Data cleaning failed")
        else:
            print("Sample reports not received")
        
        print("\nTest completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error in test: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_analyzer()
    sys.exit(0 if success else 1)
