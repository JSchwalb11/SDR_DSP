import subprocess
import smtplib, ssl

<<<<<<< HEAD
def send_email(notif):
=======

def send_email(message):
>>>>>>> 515f4ceb497413324d21acdee7f8fedf554302c5
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sdr784581@gmail.com"  # Enter your address
    receiver_email = "joey.schwalb@gmail.com"  # Enter receiver address
    password = "Mukherjee"
    msg = message

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
<<<<<<< HEAD
        server.sendmail(sender_email, receiver_email, message)

if __name__ == "__main__":
  step = (1080-880)//100
  print(step)

  start_freq = 881
  end_freq = 1081

  n_samps = 30e6

  for freq in range(start_freq, end_freq, step):
      command = "uhd_rx_cfile -f {0} -N {1} /home/sdr/git/SDR_DSP/IQ_data/5_IQ_data/{2}_fm.bin".format(freq, n_samps, freq)
      subprocess.call(command, shell=True)
  
  send_email("Done monitoring band")
=======
        server.sendmail(sender_email, receiver_email, msg)

if __name__ == '__main__':

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
>>>>>>> 515f4ceb497413324d21acdee7f8fedf554302c5
