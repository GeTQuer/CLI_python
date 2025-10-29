import argparse
#для запуска:
# python main.py --package argparse --repo-url https://github.com/GeTQuer/CLI_python.git --repo-path CLI --test-repo --version v1 --output succesful --max-depth 1

def main():
    parser = argparse.ArgumentParser(description='Dependency graph visualizer')

    parser.add_argument('--package', required=True, help='Package name')
    parser.add_argument('--repo-url', help='Repository URL')
    parser.add_argument('--repo-path', help='Repository file path')
    parser.add_argument('--test-repo', action='store_true', help='Test repository mode')
    parser.add_argument('--version', help='Package version')
    parser.add_argument('--output', default='graph.png', help='Output image filename')
    parser.add_argument('--max-depth', type=int, default=3, help='Max dependency depth')

    args = parser.parse_args()

    repo_source = args.repo_url if args.repo_url else args.repo_path

    print("package:", args.package)
    print("repository_url:", repo_source)
    print("test_repo_mode:", args.test_repo)
    print("version:", args.version if args.version else "not specified")
    print("output_filename:", args.output)
    print("max_depth:", args.max_depth)


if __name__ == "__main__":
    main()