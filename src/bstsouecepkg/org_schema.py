schema = {
    "overview": {
        "@source-id": {
            "type": "str",
            "name": "@source-id",
            "must":1
        },
        "vcard:organization-name": {
            "type": "str",
            "name": "vcard:organization-name",
            "must":1
        },
        "vcard:organization-tradename": {
            "type": "str",
            "name": "vcard:organization-tradename",
            "must":0
        },
        "localName": {
            "type": "str",
            "name": "localName",
            "must":0
        },
        "isDomiciledIn": {
            "type": "str",
            "name": "isDomiciledIn",
            "must":1
        },
        "bst:aka": {
            "type": "list",
            "name": "bst:aka",
            "must":0
        },
        "logo": {
            "type": "str",
            "name": "logo",
            "must":0
        },
        "bst:email": {
            "type": "str",
            "name": "bst:email",
            "must":0
        },
        "hasURL": {
            "type": "str",
            "name": "hasURL",
            "must":0
        },
        "hasActivityStatus": {
            "type": "str",
            "name": "hasActivityStatus",
            "must":0
        },
        "previous_names": {
            "type": "listOfDict",
            "name": "previous_names",
            "must":0,
            "keyValue": {
                "valid_from": {
                    "type": "str",
                    "name": "valid_from",
                    "must":0
                },
                "valid_to": {
                    "type": "str",
                    "name": "valid_to",
                    "must":0
                },
                "name": {
                    "type": "str",
                    "name": "name",
                    "must":1
                }
            }
        },
        "mdaas:RegisteredAddress": {
            "type": "dict",
            "name": "mdaas:RegisteredAddress",
            "must":0,
            "keyValue": {
                "zip": {
                    "type": "str",
                    "name": "zip",
                    "must":0
                },
                "country": {
                    "type": "str",
                    "name": "country",
                    "must":0
                },
                "streetAddress": {
                    "type": "str",
                    "name": "streetAddress",
                    "must":0
                },
                "city": {
                    "type": "str",
                    "name": "city",
                    "must":0
                },
                "fullAddress": {
                    "type": "str",
                    "name": "fullAddress",
                    "must":0
                }
            }
        },
        "mdaas:PostalAddress": {
            "type": "dict",
            "name": "mdaas:PostalAddress",
            "must":0,
            "keyValue": {
                "zip": {
                    "type": "str",
                    "name": "zip",
                    "must":0
                },
                "country": {
                    "type": "str",
                    "name": "country",
                    "must":0
                },
                "streetAddress": {
                    "type": "str",
                    "name": "streetAddress",
                    "must":0
                },
                "city": {
                    "type": "str",
                    "name": "city",
                    "must":0
                },
                "fullAddress": {
                    "type": "str",
                    "name": "fullAddress",
                    "must":0
                }
            }
        },
        "mdaas:OperationalAddress": {
            "type": "dict",
            "name": "mdaas:OperationalAddress",
            "must":0,
            "keyValue": {
                "zip": {
                    "type": "str",
                    "name": "zip",
                    "must":0
                },
                "country": {
                    "type": "str",
                    "name": "country",
                    "must":0
                },
                "streetAddress": {
                    "type": "str",
                    "name": "streetAddress",
                    "must":0
                },
                "city": {
                    "type": "str",
                    "name": "city",
                    "must":0
                },
                "fullAddress": {
                    "type": "str",
                    "name": "fullAddress",
                    "must":0
                }
            }
        },
        "bst:description": {
            "type": "str",
            "name": "bst:description",
            "must":0
        },
        "size": {
            "type": "str",
            "name": "size",
            "must":0
        },
        "map": {
            "type": "str",
            "name": "map",
            "must":0
        },
        "isIncorporatedIn": {
            "type": "str",
            "name": "isIncorporatedIn",
            "must":0
        },
        "hasLatestOrganizationFoundedDate": {
            "type": "str",
            "name": "hasLatestOrganizationFoundedDate",
            "must":0
        },
        "dissolutionDate": {
            "type": "str",
            "name": "dissolutionDate",
            "must":0
        },
        "hasIPODate": {
            "type": "str",
            "name": "hasIPODate",
            "must":0
        },
        "registeredIn": {
            "type": "str",
            "name": "registeredIn",
            "must":0
        },
        "tr-org:hasRegisteredPhoneNumber": {
            "type": "str",
            "name": "tr-org:hasRegisteredPhoneNumber",
            "must":0
        },
        "hasRegisteredFaxNumber": {
            "type": "str",
            "name": "hasRegisteredFaxNumber",
            "must":0
        },
        "tr-org:hasHeadquartersPhoneNumber": {
            "type": "str",
            "name": "tr-org:hasHeadquartersPhoneNumber",
            "must":0
        },
        "tr-org:hasHeadquartersFaxNumber": {
            "type": "str",
            "name": "tr-org:hasHeadquartersFaxNumber",
            "must":0
        },
        "legislationidentifier": {
            "type": "str",
            "name": "legislationidentifier",
            "must":0
        },
        "regulator_name": {
            "type": "str",
            "name": "regulator_name",
            "must":0
        },
        "regulatorAddress": {
            "type": "dict",
            "name": "regulatorAddress",
            "must":0,
            "keyValue": {
                "fullAddress": {
                    "type": "str",
                    "name": "fullAddress",
                    "must":0
                },
                "city": {
                    "type": "str",
                    "name": "city",
                    "must":0
                },
                "country": {
                    "type": "str",
                    "name": "country",
                    "must":0
                }
            }
        },
        "regulator_url": {
            "type": "str",
            "name": "regulator_url",
            "must":0
        },
        "RegulationStatus": {
            "type": "str",
            "name": "RegulationStatus",
            "must":0
        },
        "RegulationStatusEffectiveDate": {
            "type": "str",
            "name": "RegulationStatusEffectiveDate",
            "must":0
        },
        "bst:stock_info": {
            "type": "dict",
            "name": "bst:stock_info",
            "must":0,
            "keyValue": {
                "mic_code": {
                    "type": "str",
                    "name": "mic_code",
                    "must":0
                },
                "ticket_symbol": {
                    "type": "str",
                    "name": "ticket_symbol",
                    "must":0
                },
                "main_exchange": {
                    "type": "str",
                    "name": "main_exchange",
                    "must":0
                }
            }
        },
        "bst:businessClassifier": {
            "type": "listOfDict",
            "name": "bst:businessClassifier",
            "must":0,
            "keyValue": {
                "code": {
                    "type": "str",
                    "name": "code",
                    "must":0
                },
                "description": {
                    "type": "str",
                    "name": "description",
                    "must":0
                },
                "label": {
                    "type": "str",
                    "name": "label",
                    "must":0
                }
            }
        },
        "identifiers": {
            "type": "dict",
            "name": "identifiers",
            "must":0,
            "keyValue": {
                "international_securities_identifier": {
                    "type": "str",
                    "name": "international_securities_identifier",
                    "must":0
                },
                "vat_tax_number": {
                    "type": "str",
                    "name": "vat_tax_number",
                    "must":0
                },
                "european_vat_number": {
                    "type": "str",
                    "name": "european_vat_number",
                    "must":0
                },
                "legal_entity_identifier": {
                    "type": "str",
                    "name": "legal_entity_identifier",
                    "must":0
                },
                "swift_code": {
                    "type": "str",
                    "name": "swift_code",
                    "must":0
                },
                "giin": {
                    "type": "str",
                    "name": "giin",
                    "must":0
                },
                "trade_register_number": {
                    "type": "str",
                    "name": "trade_register_number",
                    "must":0
                },
                "other_company_id_number": {
                    "type": "str",
                    "name": "other_company_id_number",
                    "must":0
                }
            }
        },
        "bst:registrationId": {
            "type": "str",
            "name": "bst:registrationId",
            "must":0
        },
        "lei:legalForm": {
            "type": "dict",
            "name": "lei:legalForm",
            "must":0,
            "keyValue": {
                "code": {
                    "type": "str",
                    "name": "code",
                    "must":0
                },
                "label": {
                    "type": "str",
                    "name": "label",
                    "must":1
                }
            }
        },
        "bst:registryURI": {
            "type": "str",
            "name": "bst:registryURI",
            "must":0
        },
        "bst:sourceLinks": {
            "type": "list",
            "name": "bst:sourceLinks",
            "must":0
        },
        "regExpiryDate": {
            "type": "str",
            "name": "regExpiryDate",
            "must":0
        },
        "shareCount": {
            "type": "str",
            "name": "shareCount",
            "must":0
        },
        "Service": {
            "type": "dict",
            "name": "Service",
            "must":0,
            "keyValue": {
                "areaServed": {
                    "type": "str",
                    "name": "areaServed",
                    "must":0
                },
                "serviceType": {
                    "type": "str",
                    "name": "serviceType",
                    "must":0
                }
            }
        },
        "@type:OpeningHoursSpecifications": {
            "type": "dict",
            "name": "@type:OpeningHoursSpecifications",
            "must":0,
            "keyValue": {
                "dayOfWeek": {
                    "type": "list",
                    "name": "dayOfWeek",
                    "must":0
                },
                "Opens": {
                    "type": "str",
                    "name": "Opens",
                    "must":0
                },
                "Closes": {
                    "type": "str",
                    "name": "Closes",
                    "must":0
                }
            }
        },
        "agent":{
            "type": "dict",
            "name": "agent",
            "must":0,
            "keyValue": {
                "@type": {
                    "type": "str",
                    "name": "@type",
                    "must":0
                },
                "name": {
                    "type": "str",
                    "name": "name",
                    "must":0
                },
                "mdaas:RegisteredAddress": {
                    "type": "dict",
                    "name": "mdaas:RegisteredAddress",
                    "must":0,
                    "keyValue": {
                        "zip": {
                            "type": "str",
                            "name": "zip",
                            "must":0
                        },
                        "country": {
                            "type": "str",
                            "name": "country",
                            "must":0
                        },
                        "streetAddress": {
                            "type": "str",
                            "name": "streetAddress",
                            "must":0
                        },
                        "city": {
                            "type": "str",
                            "name": "city",
                            "must":0
                        },
                        "fullAddress": {
                            "type": "str",
                            "name": "fullAddress",
                            "must":0
                        }
                    }
                }
            }
        },
        "classOfShares":{
            "type": "listOfDict",
            "name": "classOfShares",
            "must":0,
            "keyValue": {
                "class": {
                    "type": "str",
                    "name": "class",
                    "must":1
                },
                "count": {
                    "type": "str",
                    "name": "count",
                    "must":1
                },
                "year": {
                    "type": "str",
                    "name": "year",
                    "must":0
                }
            }
        },
        "sourceDate": {
            "type": "str",
            "name": "sourceDate",
            "must":0
        }
    },
    "documents": {
        "date": {
            "type": "str",
            "name": "date",
            "must":0
        },
        "description": {
            "type": "str",
            "name": "description",
            "must":0
        },
        "url": {
            "type": "str",
            "name": "url",
            "must":1
        }
    },
    "officership": {
        "name": {
            "type": "str",
            "name": "name",
            "must":1
        },
        "type": {
            "type": "str",
            "name": "type",
            "must":0
        },
        "address": {
            "type": "dict",
            "name": "address",
            "must":0,
            "keyValue": {
                "address_line_1": {
                    "type": "str",
                    "name": "address_line_1",
                    "must":0
                },
                "postal_code": {
                    "type": "str",
                    "name": "postal_code",
                    "must":0
                }
            }
        },
        "officer_role": {
            "type": "str",
            "name": "officer_role",
            "must":0
        },
        "occupation": {
            "type": "str",
            "name": "occupation",
            "must":0
        },
        "status": {
            "type": "str",
            "name": "status",
            "must":0
        },
        "country_of_residence": {
            "type": "str",
            "name": "country_of_residence",
            "must":0
        },
        "description": {
            "type": "str",
            "name": "description",
            "must":0
        },
        "date_of_birth": {
            "type": "dict",
            "name": "date_of_birth",
            "must":0,
            "keyValue": {
                "year": {
                    "type": "str",
                    "name": "year",
                    "must":0
                },
                "month": {
                    "type": "str",
                    "name": "month",
                    "must":0
                },
                "day": {
                    "type": "str",
                    "name": "day",
                    "must":0
                }
            }
        },
        "date_of_incorporation": {
            "type": "dict",
            "name": "date_of_incorporation",
            "must":0,
            "keyValue": {
                "year": {
                    "type": "str",
                    "name": "year",
                    "must":0
                },
                "month": {
                    "type": "str",
                    "name": "month",
                    "must":0
                },
                "day": {
                    "type": "str",
                    "name": "day",
                    "must":0
                }
            }
        },
        "information_source": {
            "type": "str",
            "name": "information_source",
            "must":0
        },
        "information_provider": {
            "type": "str",
            "name": "information_provider",
            "must":0
        },
        "sourceDate": {
            "type": "str",
            "name": "sourceDate",
            "must":0
        }
    },
    "branches": {
        "@sourceReferenceID": {
            "type": "str",
            "name": "@sourceReferenceID",
            "must":0
        },
        "entity_type": {
            "type": "str",
            "name": "entity_type",
            "must":0
        },
        "isDomiciledIn": {
            "type": "str",
            "name": "isDomiciledIn",
            "must":0
        },
        "vcard:organization-name": {
            "type": "str",
            "name": "vcard:organization-name",
            "must":1
        },
        "mdaas:RegisteredAddress": {
            "type": "dict",
            "name": "mdaas:RegisteredAddress",
            "must":0,
            "keyValue": {
                "country": {
                    "type": "str",
                    "name": "country",
                    "must":0
                },
                "city": {
                    "type": "str",
                    "name": "city",
                    "must":0
                },
                "zip": {
                    "type": "str",
                    "name": "zip",
                    "must":0
                },
                "streetAddress": {
                    "type": "str",
                    "name": "streetAddress",
                    "must":0
                },
                "fullAddress": {
                    "type": "str",
                    "name": "fullAddress",
                    "must":0
                }
                
            }
        }
    },
    "subsidiaries": {
        "@sourceReferenceID": {
            "type": "str",
            "name": "@sourceReferenceID",
            "must":0
        },
        "entity_type": {
            "type": "str",
            "name": "entity_type",
            "must":0
        },
        "isDomiciledIn": {
            "type": "str",
            "name": "isDomiciledIn",
            "must":0
        },
        "vcard:organization-name": {
            "type": "str",
            "name": "vcard:organization-name",
            "must":1
        },
        "hasURL": {
            "type": "str",
            "name": "hasURL",
            "must":0
        },
        "mdaas:RegisteredAddress": {
            "type": "dict",
            "name": "mdaas:RegisteredAddress",
            "must":0,
            "keyValue": {
                "country": {
                    "type": "str",
                    "name": "country",
                    "must":0
                },
                "city": {
                    "type": "str",
                    "name": "city",
                    "must":0
                },
                "zip": {
                    "type": "str",
                    "name": "zip",
                    "must":0
                },
                "streetAddress": {
                    "type": "str",
                    "name": "streetAddress",
                    "must":0
                },
                "fullAddress": {
                    "type": "str",
                    "name": "fullAddress",
                    "must":0
                }
                
            }
        },
        "relation": {
            "type": "dict",
            "name": "relation",
            "must":1,
            "keyValue": {
                "natureOfControl": {
                    "type": "str",
                    "name": "natureOfControl",
                    "must":1
                },
                "from": {
                    "type": "str",
                    "name": "from",
                    "must":0
                },
                "source": {
                    "type": "str",
                    "name": "source",
                    "must":1
                }
            }
        }
    },
    "Financial_Information": {
        "Summary_Financial_data": {
            "type": "listOfDict",
            "name": "Summary_Financial_data",
            "must":0,
            "keyValue": {
                "source": {
                    "type": "str",
                    "name": "source",
                    "must":0
                },
                "inner_source": {
                    "type": "str",
                    "name": "inner_source",
                    "must":0
                },
                "summary": {
                    "type": "dict",
                    "name": "summary",
                    "must":0,
                    "keyValue": {
                        "currency": {
                            "type": "str",
                            "name": "currency",
                            "must":0
                        },
                        "balance_sheet": {
                            "type": "dict",
                            "name": "balance_sheet",
                            "must":0,
                            "keyValue": {
                                "date": {
                                    "type": "str",
                                    "name": "date",
                                    "must":0
                                },
                                "market_capitalization": {
                                    "type": "str",
                                    "name": "market_capitalization",
                                    "must":0
                                },
                                "current_assets": {
                                    "type": "str",
                                    "name": "current_assets",
                                    "must":0
                                },
                                "non_current_assets": {
                                    "type": "str",
                                    "name": "non_current_assets",
                                    "must":0
                                },
                                "total_assets": {
                                    "type": "str",
                                    "name": "total_assets",
                                    "must":0
                                },
                                "current_liabilities": {
                                    "type": "str",
                                    "name": "current_liabilities",
                                    "must":0
                                },
                                "non_current_liabilities": {
                                    "type": "str",
                                    "name": "non_current_liabilities",
                                    "must":0
                                },
                                "total_liabilities": {
                                    "type": "str",
                                    "name": "total_liabilities",
                                    "must":0
                                },
                                "authorized_share_capital": {
                                    "type": "str",
                                    "name": "authorized_share_capital",
                                    "must":0
                                },
                                "paid_up_share_capital": {
                                    "type": "str",
                                    "name": "paid_up_share_capital",
                                    "must":0
                                },
                                "issued_share_capital": {
                                    "type": "str",
                                    "name": "issued_share_capital",
                                    "must":0
                                },
                                "shareholders_funds": {
                                    "type": "str",
                                    "name": "shareholders_funds",
                                    "must":0
                                }
                                
                            }
                        },
                        "income_statement": {
                            "type": "dict",
                            "name": "income_statement",
                            "must":0,
                            "keyValue": {
                                "period": {
                                    "type": "str",
                                    "name": "period",
                                    "must":0
                                },
                                "revenue": {
                                    "type": "str",
                                    "name": "revenue",
                                    "must":0
                                },
                                "profit": {
                                    "type": "str",
                                    "name": "profit",
                                    "must":0
                                },
                                "cash_flow_from_operations": {
                                    "type": "str",
                                    "name": "cash_flow_from_operations",
                                    "must":0
                                },
                                "cash_flow_from_investing_activities": {
                                    "type": "str",
                                    "name": "cash_flow_from_investing_activities",
                                    "must":0
                                },
                                "cash_flow_from_financing_activities": {
                                    "type": "str",
                                    "name": "cash_flow_from_financing_activities",
                                    "must":0
                                }
                            }
                        }
                    }
                }
            }
        },
        "financial_statements": {
            "type": "dict",
            "name": "financial_statements",
            "must":0,
            "keyValue": {
                "balance_sheet": {
                    "type": "listOfDict",
                    "name": "balance_sheet",
                    "must":0,
                    "keyValue": {
                        "date": {
                            "type": "str",
                            "name": "date",
                            "must":0
                        },
                        "section": {
                            "type": "str",
                            "name": "section",
                            "must":0
                        },
                        "line_item_desc": {
                            "type": "str",
                            "name": "line_item_desc",
                            "must":1
                        },
                        "line_item_amount": {
                            "type": "str",
                            "name": "line_item_amount",
                            "must":1
                        }
                    }
                },
                "income_statement": {
                    "type": "listOfDict",
                    "name": "income_statement",
                    "must":0,
                    "keyValue": {
                        "period": {
                            "type": "str",
                            "name": "period",
                            "must":0
                        },
                        "line_item_desc": {
                            "type": "str",
                            "name": "line_item_desc",
                            "must":1
                        },
                        "line_item_amount": {
                            "type": "str",
                            "name": "line_item_amount",
                            "must":1
                        }
                    }
                },
                "cash_flow_statement": {
                    "type": "listOfDict",
                    "name": "cash_flow_statement",
                    "must":0,
                    "keyValue": {
                        "period": {
                            "type": "str",
                            "name": "period",
                            "must":0
                        },
                        "line_item_desc": {
                            "type": "str",
                            "name": "line_item_desc",
                            "must":1
                        },
                        "line_item_amount": {
                            "type": "str",
                            "name": "line_item_amount",
                            "must":1
                        }
                    }
                }
            }
        },
        "stocks_information": {
            "type": "listOfDict",
            "name": "stocks_information",
            "must":0,
            "keyValue": {
                "stock_id": {
                    "type": "str",
                    "name": "stock_id",
                    "must":0
                },
                "stock_name": {
                    "type": "str",
                    "name": "stock_name",
                    "must":0
                },
                "current": {
                    "type": "dict",
                    "name": "current",
                    "must":0,
                    "keyValue": {
                        "data_date": {
                            "type": "str",
                            "name": "data_date",
                            "must":0
                        },
                        "exchange_currency": {
                            "type": "str",
                            "name": "exchange_currency",
                            "must":0
                        },
                        "open_price": {
                            "type": "str",
                            "name": "open_price",
                            "must":0
                        },
                        "close_price": {
                            "type": "str",
                            "name": "close_price",
                            "must":0
                        },
                        "day_range": {
                            "type": "str",
                            "name": "day_range",
                            "must":0
                        },
                        "volume": {
                            "type": "str",
                            "name": "volume",
                            "must":0
                        },
                        "prev_close_price": {
                            "type": "str",
                            "name": "prev_close_price",
                            "must":0
                        },
                        "market_capitalization": {
                            "type": "str",
                            "name": "market_capitalization",
                            "must":0
                        },
                        "earnings_date": {
                            "type": "str",
                            "name": "earnings_date",
                            "must":0
                        },
                        "pe_ratio": {
                            "type": "str",
                            "name": "pe_ratio",
                            "must":0
                        },
                        "52_week_range": {
                            "type": "str",
                            "name": "52_week_range",
                            "must":0
                        },
                        "ytd_change": {
                            "type": "str",
                            "name": "ytd_change",
                            "must":0
                        }
                    }
                },
                "historical_prices":{
                    "type": "listOfDict",
                    "name": "historical_prices",
                    "must":0,
                    "keyValue": {
                        "data_date": {
                            "type": "str",
                            "name": "data_date",
                            "must":0
                        },
                        "open_price": {
                            "type": "str",
                            "name": "open_price",
                            "must":0
                        },
                        "close_price": {
                            "type": "str",
                            "name": "close_price",
                            "must":0
                        },
                        "volume": {
                            "type": "str",
                            "name": "volume",
                            "must":0
                        },
                        "day_range": {
                            "type": "str",
                            "name": "day_range",
                            "must":0
                        }
                    }
                }
            }
        }
    }
}