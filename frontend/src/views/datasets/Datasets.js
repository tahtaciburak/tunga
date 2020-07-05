import React, { useEffect, useState, createRef } from 'react'
import { CCol,  CBadge,
    CCard,
    CCardBody,
    CCardHeader,
    CDataTable,
    CButton,
    CRow } from '@coreui/react'
    
import usersData from '../users/UsersData'

import translate from '../../services/i18n/Translate';
const fields = ['name','registered', 'role', 'status']

const getBadge = status => {
    switch (status) {
      case 'Active': return 'success'
      case 'Inactive': return 'secondary'
      case 'Pending': return 'warning'
      case 'Banned': return 'danger'
      default: return 'primary'
    }
  }

class Datasets extends React.Component {
    constructor(props) {
        super(props);
    }
    render(){
        return (
        <>
        <div className="card">
            <div className="card-header">
            {translate.translate("datasets.my_datasets")}
            </div>
            <div className="card-body">
            <CCol xs="12" lg="12">
          <CCard>
            <CCardHeader>
                <CButton color="success">{translate.translate("datasets.import_from_local")}</CButton>
                <CButton style={{marginLeft:10}} color="warning">{translate.translate("datasets.import_from_url")}</CButton>
                <CButton style={{marginLeft:10}} color="primary">{translate.translate("datasets.import_from_twitter")}</CButton>
                <CButton style={{marginLeft:10}} color="danger">{translate.translate("datasets.import_from_api")}</CButton>

            </CCardHeader>
            <CCardBody>
            <CDataTable
              items={usersData}
              fields={fields}
              striped
              itemsPerPage={5}
              pagination
              scopedSlots = {{
                'status':
                  (item)=>(
                    <td>
                      <CBadge color={getBadge(item.status)}>
                        {item.status}
                      </CBadge>
                    </td>
                  )

              }}
            />
            </CCardBody>
          </CCard>
        </CCol>
            </div>
        </div>
        </>
  )}
}

export default Datasets

/**
 * 
 * 
 *             <CCard>
            <CCardHeader>
              Yukleme
            </CCardHeader>
            <CCardBody>
              <CForm>
                <CInputGroup className="mb-3">
                  <CInputGroupPrepend>
                    <CInputGroupText>
                    </CInputGroupText>
                  </CInputGroupPrepend>
                  <CInput type="text" placeholder="Email" autoComplete="email" />
                  <CFormGroup row>
                  <CLabel col md={3}>Custom file input</CLabel>
                  <CCol xs="12" md="9">
                    <CInputFile custom id="custom-file-input"/>
                    <CLabel htmlFor="custom-file-input" variant="custom-file">
                      Choose file...
                    </CLabel>
                  </CCol>
                </CFormGroup>
                </CInputGroup>

              </CForm>
            </CCardBody>
          </CCard>

 */