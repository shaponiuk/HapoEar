import simple_sine_question, cli

def main():
    def f():
        return simple_sine_question.simple_sine_interval_question(14, 70, 15)
    
    cli.simple_ask_loop(f)
    _ = input()


if __name__ == '__main__':
    main()