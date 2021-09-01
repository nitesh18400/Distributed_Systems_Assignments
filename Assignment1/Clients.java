import java.io.*;
import java.net.*;
import java.util.*;
public class Clients 
{
    public static void main(String[] args) throws IOException 
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter port No. of Server:");
        int port=sc.nextInt();
        sc.nextLine();
        InetAddress ip=InetAddress.getByName("localhost");   
        Socket s = new Socket(ip, port);        // Connect to server with defined ip and port number
        DataOutputStream outpt = new DataOutputStream(s.getOutputStream());  // Data stream for sending data to server
        System.out.print("Enter Your Name:");  //Current client name
        String name= sc.nextLine();
        outpt.writeUTF(name);  // Sending name
        
        while(true)
        {
            System.out.print("Enter The message:");  // taking input from client of message
            String msg=sc.nextLine();
            outpt.writeUTF(msg);      //sending message to server 
            if(msg.equals("quit"))   //quit request
            {
                s.close(); //closing socket
                System.out.println("Connection closed");
                break;
            }
        }
        // closing various objects
        s.close();
        outpt.close();
        sc.close();

        
    }
    
}
