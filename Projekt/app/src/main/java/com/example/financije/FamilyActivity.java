package com.example.financije;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class FamilyActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_family);
    }
    public void odiDalje(View view){
        Intent intent=new Intent(FamilyActivity.this,MainActivity.class);
        startActivity(intent);
    }
}