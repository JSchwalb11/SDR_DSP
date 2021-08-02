import subprocess
import smtplib, ssl

def send_email(message):
    """
    Send email notification
    :param message: String of message to send via email
    :return:
    """
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sdr784581@gmail.com"  # Enter your address
    receiver_email = "joey.schwalb@gmail.com"  # Enter receiver address
    password = "Mukherjee"
    msg = message

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    """
    Collect entire spectrum of samples, send email notification when done.
    """
    step = (1080-880)//100
    print(step)

    start_freq = 881
    end_freq = 1081

    n_samps = 30e6

    for freq in range(start_freq, end_freq, step):
        command = "uhd_rx_cfile -f {0} -N {1} /home/joeyschwalb/PycharmProjects/SDR_DSP/IQ_data/{2}_fm.bin".format(freq, n_samps, freq)

        subprocess.call(command, shell=True)

    message = "Done Scanning FM"
    send_email(message)
