package com.example.financije;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;


public class AutoActivity extends AppCompatActivity {


    TextView ime,potrosnja;
    Button confirm;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_auto);
    }
    public void Continue(View view){
        ime=findViewById(R.id.ImeAuta);
        potrosnja=findViewById(R.id.Potrosnja);
        if(!ime.getText().toString().equals("") && !potrosnja.getText().toString().equals("") && !potrosnja.getText().toString().equals("0")){
            Toast.makeText(this, ime.getText().toString()+" sa potrosnjom "+potrosnja.getText().toString()+" je dodan", Toast.LENGTH_SHORT).show();
            Intent intent=new Intent(AutoActivity.this,FamilyActivity.class);
            startActivity(intent);
        }
        else Toast.makeText(this, "Neka od vrijednosti je neispravna", Toast.LENGTH_SHORT).show();
    }
}