import re
from typing import Dict

class LogAnalyser:

    def __init__(self, log_file) -> None:

        # Key:value pair of the pages requested along their counts
        self.page_hit = {}

        # Key:value pair of successful page requests along their counts
        self.page_hit_ok = {}

        # Key:value pair of failed page requests along their counts
        self.page_hit_ko = {}

        # Counter for total number of page requests
        self.total_requests_counter = 0

        # Counter for total number of successful page requests
        self.request_success_counter = 0

        # Key:value pair of the requests initiated from hosts and their counts
        self.host_hit = {}

        # Key:value pair of host and their respective requests
        self.host_request_count = {}

        # Pattern compilation for parsing log entry
        log_pattern = re.compile(
           r"(?P<host>[\d\.]+)\s"
           r"(?P<identity>\S*)\s"
           r"(?P<user>\S*)\s"
           r"\[(?P<time>.*?)\]\s"
           r'"'
           r"(?P<http_request_type>[A-Z]+)\s"
           r"(?P<uri>\S+)\s"
           r'HTTP/\d.\d"\s'
           r"(?P<status>\d+)\s"
           r"(?P<bytes>\S*)\s"
           r'"(?P<referer>.*?)"\s'
           r'"(?P<user_agent>.*?)"\s*')

        def log_counter(dict_data, value):
            if value in dict_data:
                dict_data[value]+=1
            else:
                dict_data[value] = 1

        # Open the logfile
        with open(log_file) as fp:
            # Read logfile per line
            for line in fp:
                data = log_pattern.match(line)

                if data:
                    self.total_requests_counter+=1                    
                    uri = data.group('uri')
                    host = data.group('host')

                    # Page hit count
                    log_counter(self.page_hit, uri)

                    # Host hit count
                    log_counter(self.host_hit, host)

                    # Host URI count
                    if host not in self.host_request_count:
                        self.host_request_count[host] = {}
                    log_counter(self.host_request_count[host], uri)
                    
                    # Check the return status of the page
                    http_return_status = int(data.group('status'))
                    if ( http_return_status >= 200 ) and ( http_return_status < 300 ):

                        # Page hit success counter
                        self.request_success_counter+=1

                        # Caching the successful page hit info
                        log_counter(self.page_hit_ok, uri)
                    else:
                        # Caching the unsuccessful/failed page hit info
                        log_counter(self.page_hit_ko, uri)


    def get_top_result(self, dict_data, count) -> Dict:
        """
        Sort dictionary data in decreasing order on the basis of the value
        """
        sorted_data = sorted(dict_data, key=dict_data.get, reverse=True)

        result = {}
        for uri in sorted_data[:count]:
            result[uri] = dict_data[uri]

        return result


    def get_http_success_percentage(self):
        """
        Percentage of successful requests (anything in the 200s and 300s range)
        """
        
        return self.request_success_counter / self.total_requests_counter * 100


    def get_http_failed_percentage(self):
        """
        Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
        """
        
        return 100.00 - self.get_http_success_percentage()


    def get_top_hosts_requests(self, host_data):
        """
        For each of the top 10 hosts, show the top 5 pages requested and the number of requests for each
        """

        for host in host_data:
            result = self.get_top_result(self.host_request_count[host], 5)
            self.show_result(host, result)


    def show_result(self, message, data) -> None:
        """
        Prints the key:value pair in data
        """

        # Display title/header
        print(message)
        for i in range(len(message)):
            print("*", end='')
        print()
    
        # Display result
        for index, uri in enumerate(data):
            print(f'{index+1}. "{uri}": {data[uri]}')
        print()
        
        return
