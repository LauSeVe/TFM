import argparse
import subprocess
import sys
import json

def main(dst, t, nthreads):
    command = ['iperf3', '-u', '-c', dst, '-t', t, '-P', nthreads, '--json']
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    sys.stdout.flush()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run iperf3 in client mode and parse JSON output.')
    parser.add_argument('dst', type=str, help='Destination server address')
    parser.add_argument('t', type=str, help='Duration of the test in seconds')
    parser.add_argument('nthreads', type=str, help='Number of parallel client threads')
    args = parser.parse_args()
    main(args.dst, args.t, args.nthreads)
