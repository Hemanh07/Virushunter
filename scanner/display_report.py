def display_report(report):
    if report:
        hash = report["sha256"]
        descp = report["type_description"]
        size = report["size"] * 10**-3
        result = report["last_analysis_results"]
        
        malicious_count = 0
        for key, values in result.items():
            key =  f'{key}'
            verdict = values['category']
            if verdict == 'undetected':
                verdict =  'undetected'
            elif verdict == 'type-unsupported':
                verdict = 'type-unsupported'

            elif verdict == 'malicious':
                malicious_count += 1
                verdict = 'malicious'
            else:
                verdict = f'{verdict}'
        
        """ if malicious_count!= 0:
            print(f'\t\t\t\t{malicious_count} antivirus found the given file malicious!!')
        elif malicious_count == 0:
            print(f'\t\t\t\t No antivirus found the given file malicious!!') """
        
        return size,hash,descp,result,malicious_count