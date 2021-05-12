import argparse
import os
import sys
from log_analyser import LogAnalyser


def main():

    # Create CLI parser
    cli_parser = argparse.ArgumentParser(description="Apache log parser")

    # List of CLI arguements

    cli_parser.add_argument(
        'Logfile',
        metavar='<log file>',
        help='Name of the file to parse')

    cli_parser.add_argument(
        '-t',
        metavar='<count>',
        type=int,
        help='List top requested pages and their count')

    cli_parser.add_argument(
        '-ts',
        metavar='<count>',
        type=int,
        help='List top successful requests and their count')

    cli_parser.add_argument(
        '-tf',
        metavar='<count>',
        type=int,
        help='List top failed requests and their count')

    cli_parser.add_argument(
        '-ps',
        action='store_true',
        help='Display percentage of successful requests')

    cli_parser.add_argument(
        '-pf',
        action='store_true',
        help='Display percentage of failed requests')

    cli_parser.add_argument(
        '-host',
        metavar='<count>',
        type=int,
        help='List hosts with top number of requests')

    args = cli_parser.parse_args()
    
    # Verify the file passed as arguement exist
    input_file = args.Logfile
    if not os.path.isfile(input_file):
        print(f'File "{input_file}" does not exist')
        sys.exit(10)
    else:

        # Create an instance of LogAnalyser
        log_result = LogAnalyser(input_file)

        # Arguement lookup and execution
        if args.t:
            result = log_result.get_top_result(log_result.page_hit, args.t)
            msg = f"Top {args.t} requested pages"
            log_result.show_result(msg, result)

        if args.ts:
            result = log_result.get_top_result(log_result.page_hit_ok, args.ts)
            msg = f"Top {args.ts} successful page requests"
            log_result.show_result(msg, result)

        if args.tf:
            result = log_result.get_top_result(log_result.page_hit_ko, args.tf)
            msg = f"Top {args.tf} unsuccessful/failed page requests"
            log_result.show_result(msg, result)

        if args.host:
            result = log_result.get_top_result(log_result.host_hit, args.host)
            msg = f"Top {args.host} host requests"
            log_result.show_result(msg, result)

            print("Top 5 URI from each host".center(50, '-'))
            log_result.get_top_hosts_requests(result)

        if args.ps:
            print(f"Overall Successful requests: {log_result.get_http_success_percentage():3.2f}%")
        
        if args.pf:
            print(f"Overall Failed requests: {log_result.get_http_failed_percentage():3.2f}%")

    
if __name__ == "__main__":
    main()
