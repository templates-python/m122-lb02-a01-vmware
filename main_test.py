import main

def test(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Total: 75.75\n"
