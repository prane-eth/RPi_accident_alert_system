import java.io.IOException;
import java.io.OutputStream;

import java.util.Enumeration;
import java.util.List;
import java.util.ArrayList;

import gnu.io.CommPort;
import gnu.io.CommPortIdentifier;
import gnu.io.PortInUseException;
import gnu.io.SerialPort;
import gnu.io.UnsupportedCommOperationException;

class ComunicacaoMovel
{
	private static final char enter = 13;
	private static final char ctrlz = 26;

	public ComunicacaoMovel()
	{
		
	}

	private CommPortIdentifier obterPortaCommSerial()
	{
		Enumeration portasComm = CommPortIdentifier.getPortIdentifiers();

		while (portasComm.hasMoreElements())
		{
			CommPortIdentifier portaComm = (CommPortIdentifier) portasComm.nextElement();

			if (portaComm.getPortType() == CommPortIdentifier.PORT_SERIAL && portaComm.getName().equals("/dev/ttyS0"))
				return (portaComm);
		}

		return (null);
	}

	public void enviarMensagemSMS(String numeroCelular, String mensagem)
	{
		CommPortIdentifier portaComm = obterPortaCommSerial();
		List<String> mensagensSIM = new ArrayList<String>();
		mensagensSIM.add("AT");
		mensagensSIM.add("ATE0");
		mensagensSIM.add("AT+CMGF=1");
		mensagensSIM.add("AT+CMGS=\"+" + numeroCelular + "\"");
		mensagensSIM.add(mensagem);

		try
		{
			SerialPort portaSerial = (SerialPort) portaComm.open("/dev/ttyS0", 2000);
			portaSerial.setSerialPortParams(9600, SerialPort.DATABITS_8, SerialPort.STOPBITS_1, SerialPort.PARITY_NONE); 

			OutputStream streamSaida = portaSerial.getOutputStream();

			for (int i = 0; i < mensagensSIM.size(); ++i)
			{
				if (i < (mensagensSIM.size() - 1))
					streamSaida.write((mensagensSIM.get(i) + enter).getBytes());
				else
					streamSaida.write((mensagensSIM.get(i) + ctrlz).getBytes());
				Thread.sleep(1000);
				streamSaida.flush();
			}

			portaSerial.close();
		}
		catch (PortInUseException excecao)
		{
			excecao.printStackTrace();
		}
		catch (IOException excecao)
		{
			excecao.printStackTrace();
		}
		catch (UnsupportedCommOperationException excecao)
		{
			excecao.printStackTrace();
		}
		catch (InterruptedException excecao)
		{
			excecao.printStackTrace();
		}
	}

	public static void main(String[] args)
	{
		ComunicacaoMovel comunicacaoMovel = new ComunicacaoMovel();
		comunicacaoMovel.enviarMensagemSMS("+5527999XXXXXX", "Test");
	}
}//https://www.onlinegdb.com/online_java_compiler#tab-stderr
